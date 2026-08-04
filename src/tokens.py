from enum import Enum, auto


class TokenType(Enum):

    # Keywords
    KEEP = auto()
    SHOW = auto()
    ASK = auto()

    WHEN = auto()
    ORWHEN = auto()
    OTHERWISE = auto()

    REPEAT = auto()
    START = auto()
    EACH = auto()

    FROM = auto()
    TO = auto()
    STEP = auto()

    YES = auto()
    NO = auto()
    EMPTY = auto()

    AND = auto()
    OR = auto()
    NOT = auto()

    RETURN = auto()

    # Data
    IDENTIFIER = auto()
    NUMBER = auto()
    STRING = auto()

    # Arithmetic
    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()
    MODULO = auto()
    POWER = auto()

    # Assignment
    ASSIGN = auto()
    PLUS_EQUAL = auto()
    MINUS_EQUAL = auto()
    STAR_EQUAL = auto()
    SLASH_EQUAL = auto()

    # Comparison
    EQUAL_EQUAL = auto()
    NOT_EQUAL = auto()
    GREATER = auto()
    GREATER_EQUAL = auto()
    LESS = auto()
    LESS_EQUAL = auto()

    # Symbols
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    LEFT_BRACKET = auto()
    RIGHT_BRACKET = auto()
    COMMA = auto()

    EOF = auto()


class Token:
    def __init__(self, token_type, value=None, line=1):
        self.type = token_type
        self.value = value
        self.line = line

    def __repr__(self):
        return f"Token({self.type}, {self.value}, Line {self.line})"


KEYWORDS = {
    "keep": TokenType.KEEP,
    "show": TokenType.SHOW,
    "ask": TokenType.ASK,

    "when": TokenType.WHEN,
    "orwhen": TokenType.ORWHEN,
    "otherwise": TokenType.OTHERWISE,

    "repeat": TokenType.REPEAT,
    "start": TokenType.START,
    "each": TokenType.EACH,
    "from": TokenType.FROM,
    "to": TokenType.TO,
    "step": TokenType.STEP,

    "yes": TokenType.YES,
    "no": TokenType.NO,
    "empty": TokenType.EMPTY,

    "and": TokenType.AND,
    "or": TokenType.OR,
    "not": TokenType.NOT,

    "return": TokenType.RETURN,
}