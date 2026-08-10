"""
PradPyLang Error System
"""


class PradPyError(Exception):
    """Base class for all PradPyLang errors."""
    pass


class LexerError(PradPyError):
    """Raised when the lexer finds an invalid token."""
    pass


class ParserError(PradPyError):
    """Raised when the parser encounters invalid syntax."""
    pass


class RuntimeError(PradPyError):
    """Raised when the interpreter encounters a runtime error."""
    pass