from lexer import Lexer
from parser import Parser
from interpreter import Interpreter
with open("examples/hello.prad", "r", encoding="utf-8") as file:
    source = file.read()
lexer = Lexer(source)
tokens = lexer.tokenize()
parser = Parser(tokens)
program = parser.parse()
interpreter = Interpreter()
interpreter.interpret(program)