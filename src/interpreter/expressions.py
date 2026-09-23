from prad_ast import (
    NumberLiteral,
    StringLiteral,
    BooleanLiteral,
    Identifier,
    BinaryExpression,
    LogicalExpression,
    UnaryExpression,
    CallExpression,
    ListLiteral,
    EmptyLiteral,
    AskExpression,
)
from errors import RuntimeError
class ExpressionInterpreter:

    def evaluate(self, expression):

        if isinstance(expression, NumberLiteral):
            return expression.value

        if isinstance(expression, StringLiteral):
            return expression.value

        if isinstance(expression, BooleanLiteral):
            return expression.value
        if isinstance(expression, EmptyLiteral):
            return None
        if isinstance(expression, AskExpression):
            prompt = self.evaluate(expression.prompt)
            return input(prompt)

        if isinstance(expression, Identifier):
            return self.environment.get(expression.name)

        if isinstance(expression, BinaryExpression):
            return self.evaluate_binary(expression)

        if isinstance(expression, LogicalExpression):
            return self.evaluate_logical(expression)

        if isinstance(expression, UnaryExpression):
            return self.evaluate_unary(expression)

        if isinstance(expression, CallExpression):
            return self.evaluate_call(expression)
        if isinstance(expression, ListLiteral):
            return [self.evaluate(element) for element in expression.elements]

        raise RuntimeError(
            f"Unsupported expression: "
            f"{type(expression).__name__}"
        )

    def evaluate_binary(self, expression):
        left = self.evaluate(expression.left)
        right = self.evaluate(expression.right)

        operator = expression.operator
        if operator.name in ( "PLUS","MINUS", "STAR", "SLASH", "MODULO"):
            if isinstance(left, bool)or isinstance(right, bool):
                raise RuntimeError(f"invalid operands for {operator.name}")
        try:
            if operator.name == "PLUS":
                return left + right

            if operator.name == "MINUS":
                return left - right

            if operator.name == "STAR":
                return left * right

            if operator.name == "SLASH":
                if right==0:
                    raise RuntimeError("division by zero")
                return left / right

            if operator.name == "MODULO":
                if right == 0:
                    raise RuntimeError("Modulo by zero")
                return left % right
        except TypeError:
            raise RuntimeError(f"invalid operands for {operator.name}")
        if operator.name in (
                "GREATER",
                "GREATER_EQUAL",
                "LESS",
                "LESS_EQUAL",
            ):
            if isinstance(left, bool) or isinstance(right, bool):
                raise RuntimeError(
                    f"Invalid operands for {operator.name}"
                )
            if isinstance(left, list)or isinstance(right, list):
                raise RuntimeError(f"invalid operands for {operator.name}")
        try:
            if operator.name == "GREATER":
                return left > right

            if operator.name == "GREATER_EQUAL":
                return left >= right

            if operator.name == "LESS":
                return left < right

            if operator.name == "LESS_EQUAL":
                return left <= right
        except TypeError:
            raise RuntimeError(f"invalid operands for {operator.name}")

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
        try:
            if operator.name == "MINUS":
                return -operand

            if operator.name == "PLUS":
                return +operand
        except:
            raise RuntimeError(f"invlid operand for{operator.name}")

        if operator.name == "NOT":
            return not operand

        raise RuntimeError(
            f"Unsupported unary operator: {operator.name}"
        )

    def evaluate_call(self, expression):
        if not isinstance(expression.callee, Identifier):
            raise RuntimeError("task name must be an identifier.")
        name = expression.callee.name
        if name == "number":
            if len(expression.arguments) != 1:
                raise RuntimeError(
                    "number() expects exactly one argument."
                )
            value = self.evaluate(expression.arguments[0])
            if isinstance(value, bool):
                raise RuntimeError(
                    "number() cannot convert a boolean."
                )
            if isinstance(value, (int, float)):
                return value
            if isinstance(value, str):
                try:
                    if "." in value:
                        return float(value)

                    return int(value)
                except ValueError:
                    raise RuntimeError(
                        f"Cannot convert '{value}' to a number."
                    )
            raise RuntimeError(
                f"Cannot convert {type(value).__name__} to a number."
            )
        if name == "boolean":
            if len(expression.arguments) != 1:
                raise RuntimeError(
                    "boolean() expects exactly one argument."
                )
            value = self.evaluate(expression.arguments[0])
            if isinstance(value, bool):
                return value
            if isinstance(value, str):
                value = value.strip().lower()
                if value == "yes":
                    return True
                if value == "no":
                    return False
            raise RuntimeError(
                f"Cannot convert '{value}' to a boolean. "
                "Use 'yes' or 'no'."
            )
        if name == "list":
            if len(expression.arguments) != 1:
                raise RuntimeError(
                    "list() expects exactly one argument."
                )
            value = self.evaluate(expression.arguments[0])
            if isinstance(value, list):
                return value
            if not isinstance(value, str):
                raise RuntimeError(
                    "list() expects a string or list."
                )
            items = value.split(",")
            result = []
            for item in items:
                item = item.strip()
                if not item:
                    continue
                try:
                    if "." in item:
                        result.append(float(item))
                    else:
                        result.append(int(item))
                    continue
                except ValueError:
                    pass
                if item.lower() == "yes":
                    result.append(True)
                    continue
                if item.lower() == "no":
                    result.append(False)
                    continue
                result.append(item)
            return result
        task = self.functions.get(name)
        from .functions import execute_task
        return execute_task(self, task, expression.arguments)