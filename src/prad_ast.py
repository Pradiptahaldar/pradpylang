class ASTNode:
    """
    Base class for every node in the Abstract Syntax Tree (AST).
    """
    pass
class Statement(ASTNode):
    """
    Base class for all statements.
    """
    pass


class Expression(ASTNode):
    """
    Base class for all expressions.
    """
    pass
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

class VariableDeclaration(Statement):
    """
    Represents:
        keep variable = value
    """

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return (
            f"VariableDeclaration("
            f"name={self.name}, "
            f"value={self.value})"
        )
class ShowStatement(Statement):
    """
    Represents:
        show(expression)
    """

    def __init__(self, expression):
        self.expression = expression

    def __repr__(self):
        return f"ShowStatement({self.expression})"
    
class Program(ASTNode):
    """
    Root node of every PradPyLang program.
    """

    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        return f"Program({self.statements})"
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