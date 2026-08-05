from tokens import Token, TokenType, KEYWORDS
from errors import LexerError

from operators import OPERATORS
from symbols import SYMBOLS


class Lexer:
    def __init__(self, source):
        self.source = source

        self.position = 0

        self.line = 1

        self.current_char = self.source[self.position] if self.source else None

    def advance(self):
        self.position += 1

        if self.position >= len(self.source):
            self.current_char = None
        else:
            self.current_char = self.source[self.position]
    def peek(self):
        next_position = self.position + 1

        if next_position >= len(self.source):
            return None

        return self.source[next_position]
    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():

            if self.current_char == '\n':
                self.line += 1

            self.advance()
#READERS
    def read_identifier(self):
        word = ""

        while (
            self.current_char is not None
            and (
                self.current_char.isalpha()
                or self.current_char.isdigit()
                or self.current_char == "_"
            )
        ):
            word += self.current_char
            self.advance()
        token_type = KEYWORDS.get(word, TokenType.IDENTIFIER)

        return Token(token_type, word, self.line)
    def read_number(self):
            number = ""
            dot_count = 0
    
            while (
                self.current_char is not None
                and (
                    self.current_char.isdigit()
                    or self.current_char == "."
                )
            ):
                if self.current_char == ".":
                    dot_count += 1
    
                    if dot_count > 1:
                        raise LexerError(
                            f"Invalid number at line {self.line}"
                        )
    
                number += self.current_char
                self.advance()
    
            return Token(TokenType.NUMBER, number, self.line)
    def read_string(self):
        string = ""

        # Skip opening quote
        self.advance()

        while self.current_char is not None and self.current_char != '"':
            string += self.current_char
            self.advance()

        if self.current_char is None:
            raise LexerError(
                f"Unterminated string at line {self.line}"
            )

        # Skip closing quote
        self.advance()

        return Token(TokenType.STRING, string, self.line)
    def read_operator(self):
        operator = self.current_char

        # Check two-character operators
        if self.peek() is not None:
            possible = operator + self.peek()

            if possible in OPERATORS:
                self.advance()
                self.advance()
                return Token(
                    OPERATORS[possible],
                    possible,
                    self.line
                )

        # Single-character operator
        self.advance()

        return Token(
            OPERATORS[operator],
            operator,
            self.line
        )
    def read_symbol(self):
        symbol = self.current_char

        self.advance()

        return Token(
            SYMBOLS[symbol],
            symbol,
            self.line
        )
    def read_comment(self):

    # Multi-line comment
        if self.peek() == "#":

            self.advance()
            self.advance()

            while self.current_char is not None:

                if (
                    self.current_char == "#"
                    and self.peek() == "#"
                ):
                    self.advance()
                    self.advance()
                    return

                self.advance()

            raise LexerError(
                f"Unterminated multi-line comment at line {self.line}"
            )

        # Single-line comment
        else:

            while (
                self.current_char is not None
                and self.current_char != "\n"
            ):
                self.advance()
    
#MAIN TOKENIZER
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
            elif self.current_char.isalpha() or self.current_char == "_":
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
                    f"Unexpected character '{self.current_char}' at line {self.line}"
                )

        tokens.append(Token(TokenType.EOF, None, self.line))

        return tokens
    
                    