"""JavaParserBase helper class for ANTLR4 Python target."""

from antlr4 import Parser


class JavaParserBase(Parser):
    """Base class for JavaParser."""

    def IsNotIdentifierAssign(self) -> bool:
        return True

    def DoLastRecordComponent(self) -> bool:
        return True
