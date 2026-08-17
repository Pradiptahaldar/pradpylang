from lexer import Lexer
from parser import Parser
from interpreter import Interpreter


source = """
keep age = 20
show(age)
show(age + 5)
"""


lexer = Lexer(source)
tokens = lexer.tokenize()

parser = Parser(tokens)
program = parser.parse()

interpreter = Interpreter()
interpreter.interpret(program)