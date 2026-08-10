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
    IN = auto()
    START = auto()
    EACH = auto()
    TASK = auto()

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