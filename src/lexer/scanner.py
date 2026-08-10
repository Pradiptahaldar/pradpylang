from lexer import lexer
from tokens import Token, TokenType
from errors import LexerError
from .keywords import KEYWORDS
from operators import OPERATORS
from runtime.symbols import SYMBOLS

def advance(lexer):
    lexer.position += 1
    if lexer.position >= len(lexer.source):
        lexer.current_char = None
    else:
        lexer.current_char = lexer.source[lexer.position]

def peek(lexer):
    next_position = lexer.position + 1

    if next_position >= len(lexer.source):
        return None

    return lexer.source[next_position]

def skip_whitespace(lexer):
    while lexer.current_char is not None and lexer.current_char.isspace():

        if lexer.current_char == "\n":
            lexer.line += 1

        advance(lexer)

def read_identifier(lexer):
    word = ""

    while (
        lexer.current_char is not None
        and (
            lexer.current_char.isalpha()
            or lexer.current_char.isdigit()
            or lexer.current_char == "_"
        )
    ):
        word += lexer.current_char
        advance(lexer)

    token_type = KEYWORDS.get(word, TokenType.IDENTIFIER)

    return Token(token_type, word, lexer.line)

def read_number(lexer):
    number = ""
    dot_count = 0

    while (
        lexer.current_char is not None
        and (
            lexer.current_char.isdigit()
            or lexer.current_char == "."
        )
    ):
        if lexer.current_char == ".":
            dot_count += 1

            if dot_count > 1:
                raise LexerError(
                    f"Invalid number at line {lexer.line}"
                )

        number += lexer.current_char
        advance(lexer)

    return Token(TokenType.NUMBER, number, lexer.line)

def read_string(lexer):
    string = ""

    # Skip opening quote
    advance(lexer)

    while (
        lexer.current_char is not None
        and lexer.current_char != '"'
    ):
        string += lexer.current_char
        advance(lexer)

    if lexer.current_char is None:
        raise LexerError(
            f"Unterminated string at line {lexer.line}"
        )

    # Skip closing quote
    advance(lexer)

    return Token(TokenType.STRING, string, lexer.line)

def read_operator(lexer):
    operator = lexer.current_char

    # Check two-character operators
    if peek(lexer) is not None:
        possible = operator + peek(lexer)

        if possible in OPERATORS:
            advance(lexer)
            advance(lexer)

            return Token(
                OPERATORS[possible],
                possible,
                lexer.line
            )

    # Single-character operator
    advance(lexer)

    return Token(
        OPERATORS[operator],
        operator,
        lexer.line
    )

def read_symbol(lexer):
    symbol = lexer.current_char

    advance(lexer)

    return Token(
        SYMBOLS[symbol],
        symbol,
        lexer.line
    )

def read_comment(lexer):

    # Multi-line comment
    if peek(lexer) == "#":

        advance(lexer)
        advance(lexer)

        while lexer.current_char is not None:

            if (
                lexer.current_char == "#"
                and peek(lexer) == "#"
            ):
                advance(lexer)
                advance(lexer)
                return

            advance(lexer)

        raise LexerError(
            f"Unterminated multi-line comment at line {lexer.line}"
        )

    # Single-line comment
    else:

        while (
            lexer.current_char is not None
            and lexer.current_char != "\n"
        ):
            advance(lexer)