from .base import Statement


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