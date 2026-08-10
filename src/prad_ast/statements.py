from .base import Statement


class ShowStatement(Statement):
    """
    Represents:
    show(expression)
    """

    def __init__(self, expression):
        self.expression = expression

    def __repr__(self):
        return f"ShowStatement({self.expression})"


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


class ReturnStatement(Statement):
    """
    Represents:
    return expression
    """

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"ReturnStatement(value={self.value})"