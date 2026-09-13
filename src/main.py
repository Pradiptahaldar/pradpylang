from lexer import Lexer
from parser import Parser
from interpreter import Interpreter
from errors import LexerError, ParserError, RuntimeError

try:
    with open ("examples/hello.prad", "r", encoding= "utf-8") as file:
        source= file.read()
    lexer= Lexer(source)
    tokens= lexer.tokenize()

    parser= Parser(tokens)
    program= parser.parse()

    interpreter= Interpreter()
    interpreter.interpret(program)
except LexerError as error:
    print(f"Lexererror: {error}")
except ParserError as error:
    print(f"Parsererror: {error}")
except RuntimeError as error:
    print(f"Runtimeerror: {error}")
