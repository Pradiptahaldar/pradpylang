from .token_types import TokenType


class Token:

    def __init__(self, token_type, value=None, line=1):
        self.type = token_type
        self.value = value
        self.line = line

    def __repr__(self):
        return f"Token({self.type}, {self.value}, Line {self.line})"