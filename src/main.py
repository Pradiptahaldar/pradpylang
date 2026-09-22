import sys

from lexer import Lexer
from parser import Parser
from interpreter import Interpreter
from errors import LexerError, ParserError, RuntimeError


def run_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            source = file.read()

        lexer = Lexer(source)
        tokens = lexer.tokenize()

        parser = Parser(tokens)
        program = parser.parse()

        interpreter = Interpreter()
        interpreter.interpret(program)

    except FileNotFoundError:
        print(f"File not found: {filename}")
        sys.exit(1)

    except LexerError as error:
        print(f"LexerError: {error}")
        sys.exit(1)

    except ParserError as error:
        print(f"ParserError: {error}")
        sys.exit(1)

    except RuntimeError as error:
        print(f"RuntimeError: {error}")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print("Usage: pradpy <file.prad>")
        sys.exit(1)

    filename = sys.argv[1]

    if not filename.endswith(".prad"):
        print("Error: PradPyLang files must have a .prad extension.")
        sys.exit(1)

    run_file(filename)


if __name__ == "__main__":
    main()