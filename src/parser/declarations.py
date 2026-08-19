from tokens import TokenType
from prad_ast import (
    Identifier,
    VariableDeclaration,
    TaskDeclaration,
)
class DeclarationParser:
    def parse_variable_declaration(self):
        self.expect(TokenType.KEEP)
        name = Identifier(
            self.expect(TokenType.IDENTIFIER).value
        )
        self.expect(TokenType.ASSIGN)
        value = self.parse_expression()
        return VariableDeclaration(name, value)
    def parse_task_declaration(self):
        self.expect(TokenType.TASK)
        name = Identifier(
            self.expect(TokenType.IDENTIFIER).value
        )
        self.expect(TokenType.LEFT_PAREN)
        parameters = []
        if self.current_token.type != TokenType.RIGHT_PAREN:
            parameters.append(
                Identifier(
                    self.expect(TokenType.IDENTIFIER).value
                )
            )
            while self.current_token.type == TokenType.COMMA:

                self.expect(TokenType.COMMA)

                parameters.append(
                    Identifier(
                        self.expect(TokenType.IDENTIFIER).value
                    )
                )

        self.expect(TokenType.RIGHT_PAREN)

        body = self.parse_block()

        return TaskDeclaration(
            name,
            parameters,
            body
        )