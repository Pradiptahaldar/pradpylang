from tokens import Token, TokenType
from errors import ParserError

from .expressions import ExpressionParser
from .statements import StatementParser
from .declarations import DeclarationParser


class Parser(
    ExpressionParser,
    StatementParser,
    DeclarationParser,
):

    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.position = 0
        self.current_token = self.tokens[self.position]

    def advance(self):
        if self.position < len(self.tokens) - 1:
            self.position += 1
            self.current_token = self.tokens[self.position]

    def expect(self, token_type: TokenType):
        if self.current_token.type != token_type:
            raise ParserError(
                f"Expected {token_type.name}, "
                f"but got {self.current_token.type.name}"
            )

        token = self.current_token
        self.advance()

        return token

    def parse(self):
        statements = []

        while self.current_token.type != TokenType.EOF:
            statements.append(self.parse_statement())

        from prad_ast import Program

        return Program(statements)