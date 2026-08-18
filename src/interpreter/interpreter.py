from runtime import Environment
from .expressions import ExpressionInterpreter
from .statements import StatementInterpreter
class Interpreter(
    ExpressionInterpreter,
    StatementInterpreter,
):

    def __init__(self):
        self.environment = Environment()

    def interpret(self, program):
        for statement in program.statements:
            self.execute_statement(statement)