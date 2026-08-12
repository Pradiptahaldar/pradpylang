from prad_ast import (
    NumberLiteral,
    StringLiteral,
    BooleanLiteral,
    Identifier,
    BinaryExpression,
    LogicalExpression,
    UnaryExpression,
    CallExpression,
)


class ExpressionInterpreter:

    def evaluate(self, expression):

        if isinstance(expression, NumberLiteral):
            return expression.value

        if isinstance(expression, StringLiteral):
            return expression.value

        if isinstance(expression, BooleanLiteral):
            return expression.value
        if isinstance(expression, BinaryExpression):
            return self.evaluate_binary(expression)

        if isinstance(expression, LogicalExpression):
            return self.evaluate_logical(expression)

        if isinstance(expression, Identifier):
            return self.environment.get(expression.name)

        if isinstance(expression, CallExpression):
            return self.evaluate_call(expression)

        raise RuntimeError(
            f"Unsupported expression: "
            f"{type(expression).__name__}"
        )
        def evaluate_binary(self, expression):
            left = self.evaluate(expression.left)
            right = self.evaluate(expression.right)

            operator = expression.operator

            if operator.name == "PLUS":
                return left + right

            if operator.name == "MINUS":
                return left - right

            if operator.name == "STAR":
                return left * right

            if operator.name == "SLASH":
                return left / right

            if operator.name == "MODULO":
                return left % right

            if operator.name == "GREATER":
                return left > right

            if operator.name == "GREATER_EQUAL":
                return left >= right

            if operator.name == "LESS":
                return left < right

            if operator.name == "LESS_EQUAL":
                return left <= right

            if operator.name == "EQUAL_EQUAL":
                return left == right

            if operator.name == "NOT_EQUAL":
                return left != right

            raise RuntimeError(
                f"Unsupported binary operator: {operator.name}"
            )

        def evaluate_logical(self, expression):
            left = self.evaluate(expression.left)

            if expression.operator.name == "AND":
                if not left:
                    return False

                return bool(self.evaluate(expression.right))

            if expression.operator.name == "OR":
                if left:
                    return True

                return bool(self.evaluate(expression.right))

            raise RuntimeError(
                f"Unsupported logical operator: "
                f"{expression.operator.name}"
            )
        def evaluate_unary(self, expression):
            operand = self.evaluate(expression.operand)

            operator = expression.operator

            if operator.name == "MINUS":
                return -operand

            if operator.name == "PLUS":
                return +operand

            if operator.name == "NOT":
                return not operand

            raise RuntimeError(
                f"Unsupported unary operator: {operator.name}"
            )
        def evaluate_call(self, expression):
            raise RuntimeError(
                "Function calls are not implemented yet"
            )