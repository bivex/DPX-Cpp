"""Base class for generated CPP14Parser implementing runtime predicates."""

from antlr4 import Parser


class CPP14ParserBase(Parser):
    """Base parser supporting semantic predicates in CPP14 grammar."""

    def IsPureSpecifierAllowed(self) -> bool:
        """Allow pure specifier (= 0) for pure virtual member declarations."""
        return True
