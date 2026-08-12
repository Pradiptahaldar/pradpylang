class Environment:

    def __init__(self):
        self.values = {}

    def define(self, name, value):
        self.values[name] = value

    def get(self, name):
        if name not in self.values:
            raise RuntimeError(
                f"Undefined variable '{name}'"
            )

        return self.values[name]

    def assign(self, name, value):
        if name not in self.values:
            raise RuntimeError(
                f"Undefined variable '{name}'"
            )

        self.values[name] = value