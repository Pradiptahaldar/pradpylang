class FunctionRegistry:
    def __init__(self):
        self.functions = {}
    def define(self, name, function):
        self.functions[name] = function
    def get(self, name):
        if name not in self.functions:
            raise RuntimeError(
                f"Undefined task '{name}'"
            )
        return self.functions[name]
class TaskReturn(Exception):
    def __init__(self, value):
        self.value = value
def execute_task(interpreter, task, arguments):
    if len(arguments) != len(task.parameters):
        raise RuntimeError(
            f"Task '{task.name.name}' expected"
            f" {len(task.parameters)} arguments, "
            f"but got {len(arguments)}."
        )
    values = [
        interpreter.evaluate(argument)
        for argument in arguments
    ]

    previous_environment = interpreter.environment

    from runtime import Environment
    interpreter.environment = Environment()

    for parameter, value in zip(task.parameters, values):
        interpreter.environment.define(
            parameter.name,
            value
        )

    try:
        for statement in task.body:
            interpreter.execute_statement(statement)
    except TaskReturn as return_signal:
        return return_signal.value
    finally:
        interpreter.environment = previous_environment

    return None