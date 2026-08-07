from lexer import Lexer
from parser import Parser
with open("../examples/hello.prad", "r") as file:
    source = file.read()

lexer = Lexer(source)
tokens = lexer.tokenize()

for token in tokens:
    print(token)

parser = Parser(tokens)
program = parser.parse()

print(program)
