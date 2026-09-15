from errors import RuntimeError
class Environment:
    def __init__(self, parent=None):
        self.values = {}
        self.parent=parent
    def define(self, name, value):
        self.values[name] = value
    def get(self, name):
        if name in self.values:
            return self.values[name]
        if self.parent is not None:
            return self.parent.get(name)
        raise RuntimeError(
            f"Undefined variable '{name}'"
        )
    def assign(self, name, value):
        if name in self.values:
            self.values[name]=value
            return
        if self.parent is not None:
            self.parent.assign(name, value)
            return
        raise RuntimeError(
            f"Undefined variable '{name}'"
        )