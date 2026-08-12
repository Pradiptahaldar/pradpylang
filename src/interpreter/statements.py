from prad_ast import (
    ShowStatement,
    VariableDeclaration,
    WhenStatement,
    RepeatStatement,
)
class StatementInterpreter:
    def execute_statement(self, statement):
        if isinstance(statement, ShowStatement):
            value = self.evaluate(statement.expression)
            print(value)

        elif isinstance(statement, VariableDeclaration):
            value = self.evaluate(statement.value)
            self.environment.define(
                statement.name.name,
                value
            )
        elif isinstance(statement, WhenStatement):
            self.execute_when(statement)

        elif isinstance(statement, RepeatStatement):
            self.execute_repeat(statement)

        else:
            raise RuntimeError(
                f"Unsupported statement: "
                f"{type(statement).__name__}"
            )
    def execute_when(self, statement):
        if self.evaluate(statement.condition):
            for body_statement in statement.body:
                self.execute_statement(body_statement)

            return

        for condition, body in statement.orwhen_branches:

            if self.evaluate(condition):
                for body_statement in body:
                    self.execute_statement(body_statement)

                return

        if statement.otherwise_body is not None:
            for body_statement in statement.otherwise_body:
                self.execute_statement(body_statement)
    def execute_repeat(self, statement):
        count = self.evaluate(statement.count)

        for _ in range(count):
            for body_statement in statement.body:
                self.execute_statement(body_statement)