from tokens import Token, TokenType
from errors import ParserError  
from prad_ast import (
    NumberLiteral,
    Program,
    StringLiteral,
    Identifier,
    VariableDeclaration,
    ShowStatement,
    BinaryExpression,
    WhenStatement,
    RepeatStatement,
    EachStatement,
    UnaryExpression,
    BooleanLiteral,
    LogicalExpression,
    CallExpression,
    TaskDeclaration,
    ReturnStatement,
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
#parse main 
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
#parse expressions start here
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


    def parse_primary(self):
        if self.current_token.type == TokenType.NUMBER:
            token = self.expect(TokenType.NUMBER)
            return NumberLiteral(token.value)

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

        raise ParserError(
            f"Expected expression, "
            f"but got {self.current_token.type.name}"
    )
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

        return WhenStatement(condition, body, orwhen_branches=orwhen_branches,otherwise_body=otherwise_body,)
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
    def parse_return_statement(self):

        self.expect(TokenType.RETURN)

        value = self.parse_expression()

        return ReturnStatement(value)