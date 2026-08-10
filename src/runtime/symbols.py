
from tokens import TokenType


SYMBOLS = {
    "(": TokenType.LEFT_PAREN,
    ")": TokenType.RIGHT_PAREN,

    "{": TokenType.LEFT_BRACE,
    "}": TokenType.RIGHT_BRACE,

    "[": TokenType.LEFT_BRACKET,
    "]": TokenType.RIGHT_BRACKET,

    ",": TokenType.COMMA,
}