from lexer import Lexer

with open("../examples/hello.prad", "r") as file:
    source = file.read()

lexer = Lexer(source)
tokens = lexer.tokenize()

for token in tokens:
    print(token)