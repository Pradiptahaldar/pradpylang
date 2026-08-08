#Abstract Syntax Tree full form
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
class WhenStatement(Statement):
    """
    Represents:
        when condition {
            code
        }
    """

    def __init__(
        self,
        condition,
        body,
        orwhen_branches=None,
        otherwise_body=None,
    ):
        self.condition = condition
        self.body = body
        self.orwhen_branches = (
            orwhen_branches if orwhen_branches else []
        )
        self.otherwise_body = otherwise_body

    def __repr__(self):
        return (
            f"WhenStatement("
            f"condition={self.condition}, "
            f"body={self.body}, "
            f"orwhen={self.orwhen_branches}, "
            f"otherwise={self.otherwise_body})"
        )
class RepeatStatement(Statement):
    """
    Represents:
        repeat times {
            code
        }
    """

    def __init__(self, count, body):
        self.count = count
        self.body = body

    def __repr__(self):
        return (
            f"RepeatStatement("
            f"count={self.count}, "
            f"body={self.body})"
        )
class EachStatement(Statement):
    """
    Represents:
        each item in iterable {
            ...
        }
    """

    def __init__(self, variable, iterable, body):
        self.variable = variable
        self.iterable = iterable
        self.body = body

    def __repr__(self):
        return (
            f"EachStatement("
            f"variable={self.variable}, "
            f"iterable={self.iterable}, "
            f"body={self.body})"
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
class TaskDeclaration(Statement):
    """
    Represents:

        task add(a, b) {
            ...
        }
    """

    def __init__(self, name, parameters, body):
        self.name = name
        self.parameters = parameters
        self.body = body

    def __repr__(self):
        return (
            f"TaskDeclaration("
            f"name={self.name}, "
            f"parameters={self.parameters}, "
            f"body={self.body})"
        )
class ReturnStatement(Statement):
    """
    Represents:

        return expression
    """

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"ReturnStatement(value={self.value})"