"""Java ANTLR4 Parser Adapter implementing ParserPort."""

from __future__ import annotations

import re
from typing import Any

from antlr4 import CommonTokenStream, InputStream

from pattern_detector.adapters.outbound.antlr.generated.java.JavaLexer import JavaLexer
from pattern_detector.adapters.outbound.antlr.generated.java.JavaParser import JavaParser
from pattern_detector.adapters.outbound.antlr.generated.java.JavaParserVisitor import JavaParserVisitor
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


class _JavaAstExtractionVisitor(JavaParserVisitor):
    """Walks the Java parse tree to extract agnostic CodeModel domain entities."""

    def __init__(self, file_path: str, source_code: str) -> None:
        super().__init__()
        self.file_path = file_path
        self.source_code = source_code
        self.package_name = "default"
        self.requires: list[str] = []
        self.imports: list[str] = []
        self.protocols: dict[str, ProtocolModel] = {}
        self.records: dict[str, RecordModel] = {}
        self.functions: dict[str, FunctionModel] = {}
        self.states: dict[str, StateModel] = {}

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
        if not ctx or not hasattr(ctx, "start") or not hasattr(ctx, "stop") or not ctx.start or not ctx.stop:
            return getattr(ctx, "getText", lambda: "")()
        start_idx = ctx.start.start
        stop_idx = ctx.stop.stop
        if start_idx is not None and stop_idx is not None and 0 <= start_idx <= stop_idx < len(self.source_code):
            return self.source_code[start_idx : stop_idx + 1]
        return ctx.getText()

    def visitPackageDeclaration(self, ctx: JavaParser.PackageDeclarationContext) -> Any:
        if ctx.qualifiedName():
            self.package_name = ctx.qualifiedName().getText()
        return self.visitChildren(ctx)

    def visitImportDeclaration(self, ctx: JavaParser.ImportDeclarationContext) -> Any:
        if ctx.qualifiedName():
            imp_text = ctx.qualifiedName().getText()
            self.imports.append(imp_text)
            # Add package dependency for cross-module graph analysis
            if "." in imp_text:
                pkg = ".".join(imp_text.split(".")[:-1])
                if pkg not in self.requires:
                    self.requires.append(pkg)
            else:
                self.requires.append(imp_text)
        return self.visitChildren(ctx)

    def visitInterfaceDeclaration(self, ctx: JavaParser.InterfaceDeclarationContext) -> Any:
        iface_name = ctx.identifier().getText() if ctx.identifier() else "AnonymousInterface"
        loc = self._get_location(ctx)
        methods: list[MethodSignature] = []

        if ctx.interfaceBody():
            for member in ctx.interfaceBody().interfaceBodyDeclaration():
                if member.interfaceMemberDeclaration() and member.interfaceMemberDeclaration().interfaceMethodDeclaration():
                    m_ctx = member.interfaceMemberDeclaration().interfaceMethodDeclaration()
                    m_name = m_ctx.interfaceCommonBodyDeclaration().identifier().getText() if m_ctx.interfaceCommonBodyDeclaration().identifier() else "unknown"
                    param_names: list[str] = []
                    params_ctx = m_ctx.interfaceCommonBodyDeclaration().formalParameters()
                    if params_ctx and params_ctx.formalParameterList():
                        fpl_items = params_ctx.formalParameterList() if isinstance(params_ctx.formalParameterList(), list) else [params_ctx.formalParameterList()]
                        for fpl in fpl_items:
                            if hasattr(fpl, "formalParameter"):
                                fps = fpl.formalParameter() if isinstance(fpl.formalParameter(), list) else [fpl.formalParameter()]
                                for p in fps:
                                    if p and hasattr(p, "variableDeclaratorId") and p.variableDeclaratorId():
                                        param_names.append(p.variableDeclaratorId().getText())
                    methods.append(MethodSignature(name=m_name, parameter_lists=[param_names], location=self._get_location(m_ctx)))

        self.protocols[iface_name] = ProtocolModel(
            name=iface_name,
            namespace=self.package_name,
            location=loc,
            methods=methods,
            docstring="",
        )
        return self.visitChildren(ctx)

    def visitClassDeclaration(self, ctx: JavaParser.ClassDeclarationContext) -> Any:
        class_name = ctx.identifier().getText() if ctx.identifier() else "AnonymousClass"
        loc = self._get_location(ctx)
        implements_list: list[str] = []
        fields: list[str] = []
        class_methods: list[FunctionModel] = []

        parent_decl = ctx.parentCtx
        is_abstract = False
        if parent_decl and hasattr(parent_decl, "classOrInterfaceModifier"):
            mods = parent_decl.classOrInterfaceModifier()
            if isinstance(mods, list):
                is_abstract = any(m.getText() == "abstract" for m in mods)
            elif mods:
                is_abstract = mods.getText() == "abstract"

        # Implemented interfaces
        if ctx.IMPLEMENTS():
            tl_list = ctx.typeList()
            if isinstance(tl_list, list):
                for tl in tl_list:
                    if hasattr(tl, "typeType"):
                        types = tl.typeType() if isinstance(tl.typeType(), list) else [tl.typeType()]
                        for t in types:
                            if t:
                                implements_list.append(t.getText())
            elif tl_list and hasattr(tl_list, "typeType"):
                types = tl_list.typeType() if isinstance(tl_list.typeType(), list) else [tl_list.typeType()]
                for t in types:
                    if t:
                        implements_list.append(t.getText())

        # Superclass
        if ctx.EXTENDS():
            tt = ctx.typeType()
            if isinstance(tt, list):
                for t in tt:
                    if t:
                        implements_list.append(t.getText())
            elif tt:
                implements_list.append(tt.getText())

        # Extract fields and methods inside class body
        if ctx.classBody():
            for decl in ctx.classBody().classBodyDeclaration():
                if decl.memberDeclaration():
                    mem = decl.memberDeclaration()
                    # Field
                    if mem.fieldDeclaration():
                        f_ctx = mem.fieldDeclaration()
                        f_type = f_ctx.typeType().getText() if f_ctx.typeType() else ""
                        for var in f_ctx.variableDeclarators().variableDeclarator():
                            f_name = var.variableDeclaratorId().getText()
                            fields.append(f_name)
                            # Check static singleton pattern
                            modifiers_text = " ".join(m.getText() for m in decl.modifier()) if decl.modifier() else ""
                            if "static" in modifiers_text and (f_type == class_name or "instance" in f_name.lower()):
                                self.states[f_name] = StateModel(
                                    name=f_name,
                                    namespace=self.package_name,
                                    location=self._get_location(var),
                                    kind="atom",
                                    is_once=True,
                                    is_dynamic=True,
                                )
                    # Method
                    elif mem.methodDeclaration():
                        m_ctx = mem.methodDeclaration()
                        m_name = m_ctx.identifier().getText() if m_ctx.identifier() else "unknown"
                        m_loc = self._get_location(m_ctx)
                        m_body = self._get_text(m_ctx.methodBody()) if m_ctx.methodBody() else ""

                        param_names = []
                        if m_ctx.formalParameters() and m_ctx.formalParameters().formalParameterList():
                            fpl_items = m_ctx.formalParameters().formalParameterList() if isinstance(m_ctx.formalParameters().formalParameterList(), list) else [m_ctx.formalParameters().formalParameterList()]
                            for fpl in fpl_items:
                                if hasattr(fpl, "formalParameter"):
                                    fps = fpl.formalParameter() if isinstance(fpl.formalParameter(), list) else [fpl.formalParameter()]
                                    for p in fps:
                                        if p and hasattr(p, "variableDeclaratorId") and p.variableDeclaratorId():
                                            param_names.append(p.variableDeclaratorId().getText())

                        # Identify called methods in body
                        calls = set(re.findall(r"\b([a-zA-Z_][a-zA-Z0-9_]*)\s*\(", m_body))

                        modifiers_text = " ".join(m.getText() for m in decl.modifier()) if decl.modifier() else ""
                        is_private = "private" in modifiers_text

                        qualified_fn_name = f"{class_name}.{m_name}"
                        fn_model = FunctionModel(
                            name=qualified_fn_name,
                            namespace=self.package_name,
                            location=m_loc,
                            parameter_lists=[param_names],
                            body_text=m_body,
                            calls=sorted(calls),
                            docstring="",
                            is_private=is_private,
                        )
                        self.functions[qualified_fn_name] = fn_model
                        class_methods.append(fn_model)

        self.records[class_name] = RecordModel(
            name=class_name,
            namespace=self.package_name,
            location=loc,
            fields=fields,
            implemented_protocols=implements_list,
            methods=class_methods,
            is_type=is_abstract,
        )

        # If abstract class, register as polymorphic protocol for pattern detection
        if is_abstract:
            self.protocols[class_name] = ProtocolModel(
                name=class_name,
                namespace=self.package_name,
                location=loc,
                methods=[MethodSignature(name=m.name.split(".")[-1], location=m.location) for m in class_methods],
                docstring="",
            )

        return self.visitChildren(ctx)

    def visitRecordDeclaration(self, ctx: Any) -> Any:
        if hasattr(ctx, "identifier") and ctx.identifier():
            rec_name = ctx.identifier().getText()
            loc = self._get_location(ctx)
            self.records[rec_name] = RecordModel(
                name=rec_name,
                namespace=self.package_name,
                location=loc,
                fields=[],
                implemented_protocols=[],
            )
        return self.visitChildren(ctx)


class JavaAntlrParserAdapter(ParserPort):
    """Parses Java source files using ANTLR4 Java grammar into agnostic CodeModel."""

    def parse_source(self, source_code: str, file_path: str = "") -> NamespaceModel:
        input_stream = InputStream(source_code)
        lexer = JavaLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = JavaParser(token_stream)

        tree = parser.compilationUnit()
        visitor = _JavaAstExtractionVisitor(file_path=file_path, source_code=source_code)
        visitor.visit(tree)

        return NamespaceModel(
            name=visitor.package_name,
            file_path=file_path,
            docstring="",
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
            import os
            from concurrent.futures import ThreadPoolExecutor

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
