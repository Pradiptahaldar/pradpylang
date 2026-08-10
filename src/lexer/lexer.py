from tokens import Token, TokenType
from errors import LexerError
from operators import OPERATORS
from runtime.symbols import SYMBOLS
from .scanner import (
    advance,
    peek,
    skip_whitespace,
    read_identifier,
    read_number,
    read_string,
    read_operator,
    read_symbol,
    read_comment,
)
class Lexer:

    def __init__(self, source):
        self.source = source
        self.position = 0
        self.line = 1
        self.current_char = (
            self.source[self.position]
            if self.source
            else None
        )

    # Scanner wrappers
    def advance(self):
        advance(self)

    def peek(self):
        return peek(self)

    def skip_whitespace(self):
        skip_whitespace(self)

    # Readers
    def read_identifier(self):
        return read_identifier(self)

    def read_number(self):
        return read_number(self)

    def read_string(self):
        return read_string(self)

    def read_operator(self):
        return read_operator(self)

    def read_symbol(self):
        return read_symbol(self)

    def read_comment(self):
        read_comment(self)

    # Main tokenizer
    def tokenize(self):
        tokens = []

        while self.current_char is not None:

            # Ignore whitespace
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            # Comments
            elif self.current_char == "#":
                self.read_comment()
                continue

            # Identifiers & Keywords
            elif (
                self.current_char.isalpha()
                or self.current_char == "_"
            ):
                tokens.append(self.read_identifier())
                continue

            # Numbers
            elif self.current_char.isdigit():
                tokens.append(self.read_number())
                continue

            # Strings
            elif self.current_char == '"':
                tokens.append(self.read_string())
                continue

            # Operators
            elif self.current_char in OPERATORS:
                tokens.append(self.read_operator())
                continue

            # Symbols
            elif self.current_char in SYMBOLS:
                tokens.append(self.read_symbol())
                continue

            # Unknown Character
            else:
                raise LexerError(
                    f"Unexpected character "
                    f"'{self.current_char}' "
                    f"at line {self.line}"
                )

        tokens.append(
            Token(TokenType.EOF, None, self.line)
        )

        return tokens