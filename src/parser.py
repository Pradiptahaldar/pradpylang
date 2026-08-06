from tokens import Token, TokenType
from errors import ParserError  
from prad_ast import (
    NumberLiteral,
    Program,
    StringLiteral,
    Identifier,
    VariableDeclaration,
    ShowStatement,
)


class Parser:

    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.position = 0
        self.current_token = self.tokens[self.position]
    def advance(self):
        if self.position < len(self.tokens) - 1:
            self.position += 1
            self.current_token = self.tokens[self.position]
    def expect(self,token_type: TokenType):
        if self.current_token.type != token_type:
            raise ParserError(
                f"Expected {token_type.name}, "
                f"but got {self.current_token.type.name}"
            )

        token = self.current_token
        self.advance()

        return token
    def parse_expression(self):
        if self.current_token.type == TokenType.NUMBER:
            token = self.expect(TokenType.NUMBER)
            return NumberLiteral(token.value)

        elif self.current_token.type == TokenType.STRING:
            token = self.expect(TokenType.STRING)
            return StringLiteral(token.value)

        elif self.current_token.type == TokenType.IDENTIFIER:
            token = self.expect(TokenType.IDENTIFIER)
            return Identifier(token.value)

        raise ParserError(
            f"Unexpected token {self.current_token.type.name}"
        )
    def parse_variable_declaration(self):

        self.expect(TokenType.KEEP)

        name = Identifier(
            self.expect(TokenType.IDENTIFIER).value
        )

        self.expect(TokenType.ASSIGN)

        value = self.parse_expression()

        return VariableDeclaration(name, value)
    def parse_show_statement(self):

        self.expect(TokenType.SHOW)

        self.expect(TokenType.LEFT_PAREN)

        expression = self.parse_expression()

        self.expect(TokenType.RIGHT_PAREN)

        return ShowStatement(expression)
    def parse(self):
        statements = []

        while self.current_token.type != TokenType.EOF:
            statements.append(self.parse_statement())

        return Program(statements)
    def parse_statement(self):

        if self.current_token.type == TokenType.KEEP:
            return self.parse_variable_declaration()
        if self.current_token.type == TokenType.SHOW:
            return self.parse_show_statement()

        raise ParserError(
            f"Unexpected token {self.current_token.type.name}"
        )