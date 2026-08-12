from errors import ParserError
from lexer import Lexer
from parser import Parser
from tokens import token
with open("../examples/hello.prad", "r") as file:
    source = file.read()

lexer = Lexer(source)
tokens = lexer.tokenize()

parser = Parser(tokens)

for token in tokens:
    print(token)

try:
    program = parser.parse()
    print(program)

except ParserError as error:
    print(f"Parser Error: {error}")
