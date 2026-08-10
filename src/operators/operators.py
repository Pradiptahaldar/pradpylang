
from tokens import TokenType


OPERATORS = {
    "=": TokenType.ASSIGN,
    "==": TokenType.EQUAL_EQUAL,

    "+": TokenType.PLUS,
    "+=": TokenType.PLUS_EQUAL,

    "-": TokenType.MINUS,
    "-=": TokenType.MINUS_EQUAL,

    "*": TokenType.STAR,
    "*=": TokenType.STAR_EQUAL,

    "/": TokenType.SLASH,
    "/=": TokenType.SLASH_EQUAL,

    "%": TokenType.MODULO,

    "<": TokenType.LESS,
    "<=": TokenType.LESS_EQUAL,

    ">": TokenType.GREATER,
    ">=": TokenType.GREATER_EQUAL,

    "!=": TokenType.NOT_EQUAL,
}