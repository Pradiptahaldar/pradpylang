from .token_types import TokenType


KEYWORDS = {
    "keep": TokenType.KEEP,
    "show": TokenType.SHOW,
    "ask": TokenType.ASK,

    "when": TokenType.WHEN,
    "orwhen": TokenType.ORWHEN,
    "otherwise": TokenType.OTHERWISE,

    "repeat": TokenType.REPEAT,
    "in": TokenType.IN,
    "start": TokenType.START,
    "each": TokenType.EACH,

    "from": TokenType.FROM,
    "to": TokenType.TO,
    "step": TokenType.STEP,

    "task": TokenType.TASK,

    "yes": TokenType.YES,
    "no": TokenType.NO,
    "empty": TokenType.EMPTY,

    "and": TokenType.AND,
    "or": TokenType.OR,
    "not": TokenType.NOT,

    "return": TokenType.RETURN,
}