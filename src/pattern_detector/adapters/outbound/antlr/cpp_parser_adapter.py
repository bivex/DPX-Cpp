"""C++14/17/20 ANTLR4 Parser Adapter implementing ParserPort."""

from __future__ import annotations

import os
import re
from concurrent.futures import ThreadPoolExecutor
from typing import Any

from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorStrategy import BailErrorStrategy

from pattern_detector.adapters.outbound.antlr.generated.cpp.CPP14Lexer import CPP14Lexer
from pattern_detector.adapters.outbound.antlr.generated.cpp.CPP14Parser import CPP14Parser
from pattern_detector.adapters.outbound.antlr.generated.cpp.CPP14ParserVisitor import CPP14ParserVisitor
from pattern_detector.domain.code_model import (
    CodeModel,
    FunctionModel,
    MethodSignature,
    NamespaceModel,
    ProtocolModel,
    RecordModel,
    StateModel,
)
from pattern_detector.domain.value_objects import SourceLocation
from pattern_detector.ports.outbound import ParserPort


def _extract_variable_accesses(
    body_text: str,
    known_variables: set[str],
) -> tuple[list[str], list[str], list[str]]:
    """Extract reads, writes, and modifications of known variables in body_text."""
    reads: list[str] = []
    writes: list[str] = []
    modifies: list[str] = []

    RESERVED_CPP = {"true", "false", "nullptr", "NULL", "std", "this", "auto", "void", "int", "char", "bool", "double", "float", "size_t", "const"}
    for var in known_variables:
        if not var or len(var) < 2 or "::" in var or var in RESERVED_CPP or not (var[0].isalpha() or var[0] == '_'):
            continue
        # Check modification (e.g. var += ..., var -= ..., var++, ++var)
        if re.search(rf"\b{re.escape(var)}\s*(?:\+=|-=|\*=|/=|%=|\+\+|--)", body_text) or re.search(
            rf"(?:\+\+|--)\s*{re.escape(var)}\b", body_text
        ):
            modifies.append(var)
            reads.append(var)
        elif re.search(rf"\b{re.escape(var)}\s*=(?!=)", body_text):
            writes.append(var)
            rhs_match = re.search(rf"\b{re.escape(var)}\s*=\s*([^;]+);", body_text)
            body_without_lval = re.sub(rf"\b{re.escape(var)}\s*=[^;]*;", "", body_text)
            if (rhs_match and re.search(rf"\b{re.escape(var)}\b", rhs_match.group(1))) or re.search(
                rf"\b{re.escape(var)}\b", body_without_lval
            ):
                reads.append(var)
        elif re.search(rf"\b{re.escape(var)}\b", body_text):
            reads.append(var)

    return (
        sorted(list(dict.fromkeys(reads))),
        sorted(list(dict.fromkeys(writes))),
        sorted(list(dict.fromkeys(modifies))),
    )


class _CppAstExtractionVisitor(CPP14ParserVisitor):
    """Walks the C++ parse tree to extract agnostic CodeModel domain entities."""

    def __init__(self, file_path: str, source_code: str) -> None:
        super().__init__()
        self.file_path = file_path
        self.source_code = source_code
        self.namespace_stack: list[str] = []
        self.captured_namespaces: list[str] = []
        self.requires: list[str] = []
        self.imports: list[str] = []
        self.protocols: dict[str, ProtocolModel] = {}
        self.records: dict[str, RecordModel] = {}
        self.functions: dict[str, FunctionModel] = {}
        self.states: dict[str, StateModel] = {}

        # Extract #include preprocessor directives
        for line in source_code.splitlines():
            line_str = line.strip()
            if line_str.startswith("#include"):
                inc_match = re.search(r'#include\s*[<"]([^>"]+)[>"]', line_str)
                if inc_match:
                    inc_file = inc_match.group(1)
                    self.imports.append(inc_file)
                    base_inc = os.path.splitext(os.path.basename(inc_file))[0]
                    if base_inc not in self.requires:
                        self.requires.append(base_inc)

    @property
    def current_namespace(self) -> str:
        return "::".join(self.namespace_stack) if self.namespace_stack else "global"

    @property
    def primary_namespace(self) -> str:
        return self.captured_namespaces[0] if self.captured_namespaces else "global"

    def _get_location(self, ctx: Any) -> SourceLocation:
        if not ctx or not hasattr(ctx, "start") or not ctx.start:
            return SourceLocation(file_path=self.file_path, line=1, column=1)
        start = ctx.start
        stop = getattr(ctx, "stop", start) or start
        return SourceLocation(
            file_path=self.file_path,
            line=start.line,
            column=start.column + 1,
            end_line=stop.line,
            end_column=getattr(stop, "column", 0) + len(getattr(stop, "text", "") or "") + 1,
        )

    def _get_text(self, ctx: Any) -> str:
        if not ctx or not hasattr(ctx, "start") or not ctx.start or not ctx.stop:
            return getattr(ctx, "getText", lambda: "")()
        start_idx = ctx.start.start
        stop_idx = ctx.stop.stop
        if start_idx is not None and stop_idx is not None and 0 <= start_idx <= stop_idx < len(self.source_code):
            return self.source_code[start_idx : stop_idx + 1]
        return ctx.getText()

    def visitNamespaceDefinition(self, ctx: Any) -> Any:
        ns_name = "anonymous"
        if hasattr(ctx, "Identifier") and ctx.Identifier():
            ns_name = ctx.Identifier().getText()
        elif hasattr(ctx, "originalNamespaceName") and ctx.originalNamespaceName():
            ns_name = ctx.originalNamespaceName().getText()

        self.namespace_stack.append(ns_name)
        if ns_name != "anonymous":
            self.captured_namespaces.append(ns_name)
        res = self.visitChildren(ctx)
        self.namespace_stack.pop()
        return res

    def visitClassSpecifier(self, ctx: Any) -> Any:
        class_name = "AnonymousClass"
        head = ctx.classHead()
        if head and head.classHeadName():
            class_name = head.classHeadName().getText()

        loc = self._get_location(ctx)
        implements_list: list[str] = []
        fields: list[str] = []
        class_methods: list[FunctionModel] = []
        pure_virtual_methods: list[MethodSignature] = []

        # Base classes inheritance
        if head and head.baseClause():
            base_specifiers = head.baseClause().baseSpecifierList().baseSpecifier()
            if not isinstance(base_specifiers, list):
                base_specifiers = [base_specifiers]
            for bs in base_specifiers:
                base_type_name = (
                    bs.baseTypeSpecifier().getText()
                    if hasattr(bs, "baseTypeSpecifier") and bs.baseTypeSpecifier()
                    else bs.getText()
                )
                # Strip virtual / public / protected / private keywords
                clean_base = re.sub(r"\b(public|protected|private|virtual)\b", "", base_type_name).strip()
                if clean_base:
                    implements_list.append(clean_base)

        # Inspect class body members
        if ctx.memberSpecification():
            try:
                member_specs = ctx.memberSpecification().memberDeclaration()
                if not isinstance(member_specs, list):
                    member_specs = [member_specs] if member_specs else []
            except (AttributeError, TypeError):
                member_specs = []

            for mdecl in member_specs:
                mdecl_text = self._get_text(mdecl)

                # Check pure virtual method (= 0)
                is_pure_virtual = "= 0" in mdecl_text or "pureSpecifier" in str(type(mdecl))

                # Parameter extraction
                param_match = re.search(r"\(([^)]*)\)", mdecl_text)
                param_list = [p.strip() for p in param_match.group(1).split(",") if p.strip()] if param_match else []

                # Member functions / methods
                if hasattr(mdecl, "functionDefinition") and mdecl.functionDefinition():
                    fdef = mdecl.functionDefinition()
                    decltor = fdef.declarator()
                    fn_name = decltor.getText() if decltor else "unknown"
                    fn_name_clean = fn_name.split("(")[0].strip()
                    m_loc = self._get_location(fdef)
                    m_body = self._get_text(fdef.functionBody()) if fdef.functionBody() else ""
                    calls = set(re.findall(r"\b([a-zA-Z_][a-zA-Z0-9_]*)\s*\(", m_body))

                    qualified_fn_name = f"{class_name}::{fn_name_clean}"
                    fn_model = FunctionModel(
                        name=qualified_fn_name,
                        namespace=self.current_namespace,
                        location=m_loc,
                        parameter_lists=[param_list],
                        body_text=m_body,
                        calls=sorted(calls),
                        docstring="",
                        is_private="private" in mdecl_text,
                    )
                    class_methods.append(fn_model)
                    self.functions[qualified_fn_name] = fn_model

                    # Check Meyers Singleton (static ClassName& getInstance() { static ClassName instance; return instance; })
                    if "static" in mdecl_text and (
                        "instance" in fn_name_clean.lower() or "get" in fn_name_clean.lower()
                    ) and (f"static {class_name}" in m_body or "static auto" in m_body or "return instance" in m_body):
                        self.states[f"{class_name}::instance"] = StateModel(
                            name=f"{class_name}::instance",
                            namespace=self.current_namespace,
                            location=m_loc,
                            kind="atom",
                            is_once=True,
                            is_dynamic=True,
                        )
                else:
                    # Method declaration in header (e.g. virtual void run() = 0;)
                    if "(" in mdecl_text and ";" in mdecl_text:
                        match = re.search(r"([a-zA-Z_][a-zA-Z0-9_]*)\s*\(", mdecl_text)
                        if match:
                            m_name = match.group(1)
                            m_sig = MethodSignature(name=m_name, location=self._get_location(mdecl))
                            if is_pure_virtual:
                                pure_virtual_methods.append(m_sig)

                            qualified_fn_name = f"{class_name}::{m_name}"
                            fn_model = FunctionModel(
                                name=qualified_fn_name,
                                namespace=self.current_namespace,
                                location=self._get_location(mdecl),
                                parameter_lists=[[]],
                                body_text=mdecl_text,
                                calls=[],
                                is_private="private" in mdecl_text,
                            )
                            class_methods.append(fn_model)
                            self.functions[qualified_fn_name] = fn_model

                    # Field declaration
                    elif ";" in mdecl_text and not mdecl_text.startswith("typedef"):
                        f_matches = re.findall(r"([a-zA-Z_][a-zA-Z0-9_]*)\s*;", mdecl_text)
                        for fm in f_matches:
                            fields.append(fm)
                            # Static instance pointer (e.g. static ClassName* instance;)
                            if "static" in mdecl_text and (class_name in mdecl_text or "instance" in fm.lower()):
                                self.states[f"{class_name}::{fm}"] = StateModel(
                                    name=f"{class_name}::{fm}",
                                    namespace=self.current_namespace,
                                    location=self._get_location(mdecl),
                                    kind="atom",
                                    is_once=True,
                                    is_dynamic=True,
                                )

        is_abstract = len(pure_virtual_methods) > 0 or "virtual" in self._get_text(ctx) and "= 0" in self._get_text(ctx)

        self.records[class_name] = RecordModel(
            name=class_name,
            namespace=self.current_namespace,
            location=loc,
            fields=fields,
            implemented_protocols=implements_list,
            methods=class_methods,
            is_type=is_abstract,
        )

        # If abstract base class / pure interface, register as protocol
        if is_abstract or (class_name.startswith("I") and len(class_methods) > 0):
            all_sigs = [MethodSignature(name=m.name.split("::")[-1], location=m.location) for m in class_methods]
            self.protocols[class_name] = ProtocolModel(
                name=class_name,
                namespace=self.current_namespace,
                location=loc,
                methods=pure_virtual_methods if pure_virtual_methods else all_sigs,
                docstring="",
            )

        return self.visitChildren(ctx)

    def visitFunctionDefinition(self, ctx: Any) -> Any:
        try:
            decltor = ctx.declarator()
            if decltor:
                fn_name = decltor.getText()
                fn_name_clean = fn_name.split("(")[0].strip()
                if fn_name_clean and fn_name_clean not in ("main",) and fn_name_clean not in self.functions:
                    loc = self._get_location(ctx)
                    body_text = self._get_text(ctx.functionBody()) if ctx.functionBody() else ""
                    calls = sorted(set(re.findall(r"\b([a-zA-Z_][a-zA-Z0-9_]*)\s*\(", body_text)))
                    param_match = re.search(r"\(([^)]*)\)", fn_name)
                    param_list = [p.strip() for p in param_match.group(1).split(",") if p.strip()] if param_match else []

                    fn_model = FunctionModel(
                        name=fn_name_clean,
                        namespace=self.current_namespace,
                        location=loc,
                        parameter_lists=[param_list],
                        body_text=body_text,
                        calls=calls,
                        docstring="",
                    )
                    self.functions[fn_name_clean] = fn_model
        except Exception:
            pass
        return self.visitChildren(ctx)

    def visitSimpleDeclaration(self, ctx: Any) -> Any:
        try:
            decl_text = self._get_text(ctx).strip()
            if ";" in decl_text and not decl_text.startswith("typedef") and not decl_text.startswith("using"):
                vm = re.search(
                    r"\b(?:extern\s+)?(?:int|double|float|char|bool|long|short|size_t|std::string|auto|[A-Za-z0-9_:]+)\s+([A-Za-z0-9_]+)\s*(?:=\s*[^;]+)?\s*;",
                    decl_text,
                )
                if vm:
                    v_name = vm.group(1)
                    if v_name not in ("default", "delete", "const", "return", "auto") and v_name not in self.states:
                        self.states[v_name] = StateModel(
                            name=v_name,
                            namespace=self.current_namespace,
                            location=self._get_location(ctx),
                            kind="atom",
                        )
        except Exception:
            pass
        return self.visitChildren(ctx)


class CppAntlrParserAdapter(ParserPort):
    """Parses C++ (C++14/17/20) source and header files using ANTLR4 into agnostic CodeModel."""

    def _clean_source(self, source_code: str) -> str:
        """Pre-clean preprocessor directives, macros and noise that prevent AST recognition."""
        cleaned = re.sub(r"#\s*(?:pragma|define|undef|ifdef|ifndef|endif|else|elif|line)\b[^\n]*", "", source_code)
        cleaned = re.sub(r"\b[A-Z0-9_]+_(?:API|EXPORT|INLINE|NOEXCEPT|CONSTEXPR|NODISCARD)\b", "", cleaned)
        cleaned = re.sub(r"\b(?:SPDLOG_[A-Z0-9_]+|Q_OBJECT|Q_SIGNALS|Q_SLOTS|GTEST_DISALLOW_[A-Z0-9_]+)\b", "", cleaned)
        return cleaned

    def parse_source(self, source_code: str, file_path: str = "") -> NamespaceModel:
        # Fast path for large, templated, or macro-heavy files to prevent ANTLR ATN backtracking
        if (
            len(source_code) > 10_000
            or "#define" in source_code
            or "#ifdef" in source_code
            or "#if" in source_code
            or "__declspec" in source_code
            or "__attribute__" in source_code
            or "template" in source_code
        ):
            return self._fallback_regex_parse(source_code, file_path)

        cleaned_code = self._clean_source(source_code)
        input_stream = InputStream(cleaned_code)
        lexer = CPP14Lexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = CPP14Parser(token_stream)
        parser._errHandler = BailErrorStrategy()

        try:
            tree = parser.translationUnit()
            visitor = _CppAstExtractionVisitor(file_path=file_path, source_code=source_code)
            visitor.visit(tree)

            # Run Def-Use data flow variable access analysis for all functions
            all_known_vars = set(visitor.states.keys())
            for r in visitor.records.values():
                all_known_vars.update(r.fields)

            for fn in visitor.functions.values():
                r_vars, w_vars, m_vars = _extract_variable_accesses(fn.body_text, all_known_vars)
                fn.reads_variables = r_vars
                fn.writes_variables = w_vars
                fn.modifies_variables = m_vars

            return NamespaceModel(
                name=visitor.primary_namespace,
                file_path=file_path,
                docstring="",
                requires=visitor.requires,
                imports=visitor.imports,
                protocols=visitor.protocols,
                records=visitor.records,
                functions=visitor.functions,
                states=visitor.states,
            )
        except (RuntimeError, ValueError, AttributeError, Exception):  # noqa: BLE001
            # Fallback regex parser if complex macro-heavy C++ translation unit fails full AST
            return self._fallback_regex_parse(source_code, file_path)

    def _fallback_regex_parse(self, source_code: str, file_path: str) -> NamespaceModel:
        """Robust fallback AST extractor for complex macro or template-heavy C++ headers."""
        visitor = _CppAstExtractionVisitor(file_path=file_path, source_code=source_code)

        # Extract namespace
        ns_match = re.search(r"\bnamespace\s+([a-zA-Z0-9_:]+)", source_code)
        ns_name = ns_match.group(1) if ns_match else "global"

        # Pre-clean comments and macros for clean brace navigation
        cleaned = re.sub(r"/\*.*?\*/", "", source_code, flags=re.DOTALL)
        cleaned = re.sub(r"//[^\n]*", "", cleaned)
        cleaned = re.sub(r"#\s*(?:pragma|define|undef|ifdef|ifndef|endif|else|elif|line)\b[^\n]*", "", cleaned)

        CONTROL_KEYWORDS = {
            "if",
            "for",
            "while",
            "switch",
            "catch",
            "return",
            "sizeof",
            "decltype",
            "typeid",
            "dynamic_cast",
            "static_cast",
            "reinterpret_cast",
            "const_cast",
            "alignof",
            "lock",
            "throw",
            "case",
            "new",
            "delete",
            "final",
            "override",
            "const",
            "explicit",
        }

        pattern = re.compile(
            r"\b(?:class|struct)\s+(?:(?:alignas\([^)]*\)|[A-Z0-9_]+_API|[A-Z0-9_]+_EXPORT|SPDLOG_API)\s+)?([A-Za-z0-9_]+)(?:\s+final)?(?:\s*:\s*([^{]+))?\s*\{"
        )
        for cm in pattern.finditer(cleaned):
            c_name = cm.group(1)
            c_bases_raw = cm.group(2) or ""

            bases = [
                re.sub(r"\b(public|protected|private|virtual)\b", "", b).strip()
                for b in c_bases_raw.split(",")
                if b.strip()
            ]

            loc = SourceLocation(file_path=file_path, line=1, column=1)
            start_idx = cm.end()
            depth = 1
            pos = start_idx
            while pos < len(cleaned) and depth > 0:
                ch = cleaned[pos]
                if ch == "{":
                    depth += 1
                elif ch == "}":
                    depth -= 1
                pos += 1
            c_body = cleaned[start_idx : pos - 1]

            # Methods inside class body
            methods: list[FunctionModel] = []
            pure_methods: list[MethodSignature] = []
            fields: list[str] = []

            # Extract fields
            for f_match in re.finditer(r"\b(?:std::(?:shared_ptr|unique_ptr)<[^>]+>|[a-zA-Z0-9_:]+)\s+([a-zA-Z0-9_]+)\s*;", c_body):
                f_name = f_match.group(1)
                if f_name not in ("default", "delete", "override", "const", "return", "auto") and f_name not in CONTROL_KEYWORDS:
                    fields.append(f_name)

            for m in re.finditer(r"\b([A-Za-z0-9_~]+)\s*\(([^)]*)\)\s*(?:const)?\s*(?:noexcept)?\s*(?:final)?\s*(?:override)?\s*(?:=\s*0|;|\{)", c_body):
                m_name = m.group(1)
                if m_name in CONTROL_KEYWORDS or m_name in fields:
                    continue

                m_params_raw = m.group(2) or ""
                is_pure = "= 0" in m.group(0)
                qualified_name = f"{c_name}::{m_name}"
                param_list = [p.strip() for p in m_params_raw.split(",") if p.strip()]

                fn = FunctionModel(
                    name=qualified_name,
                    namespace=ns_name,
                    location=loc,
                    parameter_lists=[param_list],
                    body_text=c_body,
                    calls=sorted(set(re.findall(r"\b([a-zA-Z_][a-zA-Z0-9_]*)\s*\(", c_body))),
                )
                methods.append(fn)
                visitor.functions[qualified_name] = fn
                if is_pure:
                    pure_methods.append(MethodSignature(name=m_name, location=loc))

            if "static" in c_body and ("instance" in c_body.lower() or "getinstance" in c_body.lower() or "get_instance" in c_body.lower()):
                visitor.states[f"{c_name}::instance"] = StateModel(
                    name=f"{c_name}::instance",
                    namespace=ns_name,
                    location=loc,
                    kind="atom",
                    is_once=True,
                    is_dynamic=True,
                )

            is_abstract = len(pure_methods) > 0 or "= 0" in c_body
            visitor.records[c_name] = RecordModel(
                name=c_name,
                namespace=ns_name,
                location=loc,
                fields=fields,
                implemented_protocols=bases,
                methods=methods,
                is_type=is_abstract,
            )

            if is_abstract or (c_name.startswith("I") and len(methods) > 0):
                visitor.protocols[c_name] = ProtocolModel(
                    name=c_name,
                    namespace=ns_name,
                    location=loc,
                    methods=pure_methods if pure_methods else [MethodSignature(name=m.name.split("::")[-1], location=loc) for m in methods],
                )

        # Extract global/extern variables
        var_pattern = re.compile(
            r"\b(?:extern\s+)?(?:int|double|float|char|bool|long|short|size_t|std::string|auto|[A-Za-z0-9_:]+)\s+([A-Za-z0-9_]+)\s*(?:=\s*[^;]+)?\s*;"
        )
        for vm in var_pattern.finditer(cleaned):
            v_name = vm.group(1)
            if v_name not in CONTROL_KEYWORDS and not v_name.startswith("return") and v_name not in ("default", "delete"):
                visitor.states[v_name] = StateModel(
                    name=v_name,
                    namespace=ns_name,
                    location=SourceLocation(file_path=file_path, line=1, column=1),
                    kind="atom",
                )

        # Extract free / standalone functions
        fn_pattern = re.compile(
            r"\b(?:void|int|double|float|bool|char|std::string|auto|[A-Za-z0-9_:]+(?:\s*[*&])?)\s+([A-Za-z0-9_]+)\s*\(([^)]*)\)\s*\{"
        )
        for fn_m in fn_pattern.finditer(cleaned):
            fn_name = fn_m.group(1)
            if fn_name in CONTROL_KEYWORDS or fn_name.startswith("main") or any(r.name == fn_name for r in visitor.records.values()):
                continue
            fn_params_raw = fn_m.group(2) or ""
            fn_loc = SourceLocation(file_path=file_path, line=1, column=1)

            start_idx = fn_m.end()
            depth = 1
            pos = start_idx
            while pos < len(cleaned) and depth > 0:
                ch = cleaned[pos]
                if ch == "{":
                    depth += 1
                elif ch == "}":
                    depth -= 1
                pos += 1
            fn_body = cleaned[start_idx : pos - 1]

            param_list = [p.strip() for p in fn_params_raw.split(",") if p.strip()]
            free_fn = FunctionModel(
                name=fn_name,
                namespace=ns_name,
                location=fn_loc,
                parameter_lists=[param_list],
                body_text=fn_body,
                calls=sorted(set(re.findall(r"\b([a-zA-Z_][a-zA-Z0-9_]*)\s*\(", fn_body))),
            )
            visitor.functions[fn_name] = free_fn

        # Run Def-Use data flow variable access analysis for all functions
        all_known_vars = set(visitor.states.keys())
        for r in visitor.records.values():
            all_known_vars.update(r.fields)

        for fn in visitor.functions.values():
            r_vars, w_vars, m_vars = _extract_variable_accesses(fn.body_text, all_known_vars)
            fn.reads_variables = r_vars
            fn.writes_variables = w_vars
            fn.modifies_variables = m_vars

        return NamespaceModel(
            name=ns_name,
            file_path=file_path,
            requires=visitor.requires,
            imports=visitor.imports,
            protocols=visitor.protocols,
            records=visitor.records,
            functions=visitor.functions,
            states=visitor.states,
        )

    def parse_sources(self, sources: dict[str, str], max_workers: int | None = None) -> CodeModel:
        model = CodeModel()
        if not sources:
            return model

        if len(sources) > 3:
            workers = max_workers or min(16, (os.cpu_count() or 4) * 2)
            with ThreadPoolExecutor(max_workers=workers) as executor:
                namespaces = list(
                    executor.map(lambda item: self.parse_source(item[1], file_path=item[0]), sources.items())
                )
                for ns in namespaces:
                    model.add_namespace(ns)
        else:
            for file_path, source_code in sources.items():
                ns = self.parse_source(source_code, file_path=file_path)
                model.add_namespace(ns)

        return model
