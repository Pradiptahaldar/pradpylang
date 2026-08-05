from tokens import Token, TokenType, KEYWORDS


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
    def tokenize(self):
        tokens = []

        while self.current_char is not None:

            # Ignore spaces, tabs and newlines
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            # Read identifiers and keywords
            if self.current_char.isalpha() or self.current_char == "_":
                tokens.append(self.read_identifier())
                continue

            # Unknown character
            raise Exception(
                f"Unexpected character '{self.current_char}' at line {self.line}"
            )

        tokens.append(Token(TokenType.EOF, None, self.line))

        return tokens
                    