import argparse

from fdp import Lexer
from fdp import Parser
from fdp import PDFInterpreter
from fdp import FDPFile


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('file', help='The file to run')
    args = parser.parse_args()

    file = FDPFile(args.file)
    file.read()

    lexer = Lexer(file.content)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    instructions = parser.parse()

    interpreter = PDFInterpreter(instructions, file.pdf_path)
    result = interpreter.run()

    print(result)

if __name__ == '__main__':
    main()