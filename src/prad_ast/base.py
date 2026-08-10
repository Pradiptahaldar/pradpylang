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


class Program(ASTNode):
    """
    Root node of every PradPyLang program.
    """

    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        return f"Program({self.statements})"