from .base import Expression


class NumberLiteral(Expression):
    """
    Represents a numeric value.
    """
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"NumberLiteral({self.value})"

class StringLiteral(Expression):
    """
    Represents a string value.
    """
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f'StringLiteral("{self.value}")'

class Identifier(Expression):
    """
    Represents a variable name.
    """

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Identifier({self.name})"


class BinaryExpression(Expression):
    """
    Represents binary operations like:
    a + b
    x * y
    age >= 18
    """

    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return (
            f"BinaryExpression("
            f"{self.left}, "
            f"{self.operator.name}, "
            f"{self.right})"
        )


class UnaryExpression(Expression):
    """
    Represents unary operations like:
    -age
    +age
    """

    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

    def __repr__(self):
        return (
            f"UnaryExpression("
            f"{self.operator.name}, "
            f"{self.operand})"
        )


class LogicalExpression(Expression):
    """
    Represents logical operations like:
    a and b
    a or b
    """
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right
    def __repr__(self):
        return (
            f"LogicalExpression("
            f"{self.left}, "
            f"{self.operator.name}, "
            f"{self.right})"
        )
class BooleanLiteral(Expression):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"BooleanLiteral({self.value})"
class CallExpression(Expression):
    """
    Represents a function call:
    greet("Ivan")
    calculate(10, 20)
    """
    def __init__(self, callee, arguments):
        self.callee = callee
        self.arguments = arguments
    def __repr__(self):
        return (
            f"CallExpression("
            f"callee={self.callee}, "
            f"arguments={self.arguments})"
        )
class ListLiteral(Expression):
    """
    Represents a list of expressions.
    Example:
    [1, 2, 3]
    """
    def __init__(self, elements):
        self.elements = elements
    def __repr__(self):
        return f"ListLiteral({self.elements})"