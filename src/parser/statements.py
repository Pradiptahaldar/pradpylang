from tokens import TokenType
from errors import ParserError
from prad_ast import (
    Identifier,
    ShowStatement,
    WhenStatement,
    RepeatStatement,
    EachStatement,
    ReturnStatement,
)
class StatementParser:

    def parse_statement(self):

        if self.current_token.type == TokenType.KEEP:
            return self.parse_variable_declaration()

        elif self.current_token.type == TokenType.SHOW:
            return self.parse_show_statement()

        elif self.current_token.type == TokenType.WHEN:
            return self.parse_when_statement()

        elif self.current_token.type == TokenType.REPEAT:
            return self.parse_repeat_statement()

        elif self.current_token.type == TokenType.EACH:
            return self.parse_each_statement()

        elif self.current_token.type == TokenType.TASK:
            return self.parse_task_declaration()

        elif self.current_token.type == TokenType.RETURN:
            return self.parse_return_statement()

        raise ParserError(
            f"Unexpected token {self.current_token.type.name}"
        )

    def parse_show_statement(self):

        self.expect(TokenType.SHOW)

        self.expect(TokenType.LEFT_PAREN)

        expression = self.parse_expression()

        self.expect(TokenType.RIGHT_PAREN)

        return ShowStatement(expression)

    def parse_when_statement(self):

        self.expect(TokenType.WHEN)

        condition = self.parse_expression()

        body = self.parse_block()

        orwhen_branches = []

        while self.current_token.type == TokenType.ORWHEN:

            self.expect(TokenType.ORWHEN)

            orwhen_condition = self.parse_expression()

            orwhen_body = self.parse_block()

            orwhen_branches.append(
                (orwhen_condition, orwhen_body)
            )

        otherwise_body = None

        if self.current_token.type == TokenType.OTHERWISE:

            self.expect(TokenType.OTHERWISE)

            otherwise_body = self.parse_block()

        return WhenStatement(
            condition,
            body,
            orwhen_branches=orwhen_branches,
            otherwise_body=otherwise_body,
        )

    def parse_block(self):

        self.expect(TokenType.LEFT_BRACE)

        statements = []

        while (
            self.current_token.type != TokenType.RIGHT_BRACE
            and self.current_token.type != TokenType.EOF
        ):

            statements.append(self.parse_statement())

        self.expect(TokenType.RIGHT_BRACE)

        return statements

    def parse_repeat_statement(self):

        self.expect(TokenType.REPEAT)

        count = self.parse_expression()

        body = self.parse_block()

        return RepeatStatement(count, body)

    def parse_each_statement(self):

        self.expect(TokenType.EACH)

        variable = Identifier(
            self.expect(TokenType.IDENTIFIER).value
        )

        self.expect(TokenType.IN)

        iterable = self.parse_expression()

        body = self.parse_block()

        return EachStatement(
            variable,
            iterable,
            body
        )

    def parse_return_statement(self):

        self.expect(TokenType.RETURN)

        value = self.parse_expression()

        return ReturnStatement(value)