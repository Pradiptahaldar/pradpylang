from lexer import Lexer
from parser import Parser
with open("../examples/hello.prad", "r") as file:
    source = file.read()

lexer = Lexer(source)
tokens = lexer.tokenize()

parser = Parser(tokens)
program = parser.parse()

print(program)
