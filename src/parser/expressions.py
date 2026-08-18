from tokens import TokenType
from errors import ParserError
from prad_ast import (
    NumberLiteral,
    StringLiteral,
    Identifier,
    BinaryExpression,
    UnaryExpression,
    BooleanLiteral,
    LogicalExpression,
    CallExpression,
    ListLiteral,
)
class ExpressionParser:
    def parse_expression(self):
        return self.parse_logical_or()
    def parse_comparison(self):
        left = self.parse_term()
        while self.current_token.type in (
            TokenType.GREATER,
            TokenType.GREATER_EQUAL,
            TokenType.LESS,
            TokenType.LESS_EQUAL,
            TokenType.EQUAL_EQUAL,
            TokenType.NOT_EQUAL,
        ):

            operator = self.current_token
            self.advance()
            right = self.parse_term()
            left = BinaryExpression(
                left,
                operator.type,
                right
            )

        return left

    def parse_term(self):

        left = self.parse_factor()

        while self.current_token.type in (
            TokenType.PLUS,
            TokenType.MINUS,
        ):

            operator = self.current_token
            self.advance()

            right = self.parse_factor()

            left = BinaryExpression(
                left,
                operator.type,
                right
            )

        return left

    def parse_factor(self):

        left = self.parse_unary()

        while self.current_token.type in (
            TokenType.STAR,
            TokenType.SLASH,
            TokenType.MODULO,
        ):

            operator = self.current_token
            self.advance()

            right = self.parse_unary()

            left = BinaryExpression(
                left,
                operator.type,
                right
            )

        return left

    def parse_unary(self):

        if self.current_token.type in (
            TokenType.MINUS,
            TokenType.PLUS,
            TokenType.NOT,
        ):

            operator = self.current_token
            self.advance()

            operand = self.parse_unary()

            return UnaryExpression(
                operator.type,
                operand
            )

        return self.parse_call()

    def parse_logical_and(self):

        left = self.parse_comparison()

        while self.current_token.type == TokenType.AND:

            operator = self.current_token
            self.advance()

            right = self.parse_comparison()

            left = LogicalExpression(
                left,
                operator.type,
                right
            )

        return left

    def parse_logical_or(self):

        left = self.parse_logical_and()

        while self.current_token.type == TokenType.OR:

            operator = self.current_token
            self.advance()

            right = self.parse_logical_and()

            left = LogicalExpression(
                left,
                operator.type,
                right
            )

        return left

    def parse_call(self):

        expression = self.parse_primary()

        while self.current_token.type == TokenType.LEFT_PAREN:

            self.expect(TokenType.LEFT_PAREN)

            arguments = []

            if self.current_token.type != TokenType.RIGHT_PAREN:

                arguments.append(self.parse_expression())

                while self.current_token.type == TokenType.COMMA:

                    self.expect(TokenType.COMMA)

                    arguments.append(self.parse_expression())

            self.expect(TokenType.RIGHT_PAREN)

            expression = CallExpression(
                expression,
                arguments
            )

        return expression

    def parse_primary(self):
        if self.current_token.type == TokenType.NUMBER:
            token = self.expect(TokenType.NUMBER)
            if "." in token.value:
                value = float(token.value)
            else:
                value = int(token.value)
            return NumberLiteral(value)
        elif self.current_token.type == TokenType.STRING:
            token = self.expect(TokenType.STRING)
            return StringLiteral(token.value)
        elif self.current_token.type == TokenType.IDENTIFIER:
            token = self.expect(TokenType.IDENTIFIER)
            return Identifier(token.value)
        elif self.current_token.type == TokenType.YES:
            self.advance()
            return BooleanLiteral(True)
        elif self.current_token.type == TokenType.NO:
            self.advance()
            return BooleanLiteral(False)
        elif self.current_token.type == TokenType.LEFT_PAREN:
            self.expect(TokenType.LEFT_PAREN)
            expression = self.parse_expression()
            self.expect(TokenType.RIGHT_PAREN)
            return expression
        elif self.current_token.type == TokenType.LEFT_BRACKET:
            self.expect(TokenType.LEFT_BRACKET)
            elements = []
            if self.current_token.type != TokenType.RIGHT_BRACKET:
                elements.append(self.parse_expression())
                while self.current_token.type == TokenType.COMMA:
                    self.expect(TokenType.COMMA)
                    elements.append(self.parse_expression())
            self.expect(TokenType.RIGHT_BRACKET)
            return ListLiteral(elements)
        

        raise ParserError(
            f"Expected expression, "
            f"but got {self.current_token.type.name}"
        )