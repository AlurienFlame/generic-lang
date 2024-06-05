from lark import Lark
from interpreter import GlaInterpreter
from argparse import ArgumentParser


def main():
    # Create parser and interpreter
    parser = Lark.open("grammar.ebnf", start="start", parser="lalr")
    interpreter = GlaInterpreter()

    # Load source code from file
    arg_parser = ArgumentParser()
    arg_parser.add_argument("source_file", help="The source file to compile")
    args = arg_parser.parse_args()

    source_code = None
    with open(args.source_file) as f:
        source_code = f.read()

    # Lexing step (optional)
    # tokens = parser.lex(source_code)
    # print(list(tokens))

    # Parsing step
    syntax_tree = parser.parse(source_code)
    # print(syntax_tree.pretty())

    # Interpretation step
    interpreter.transform(syntax_tree)
    print(f"Symbol table: {interpreter.symbol_table}")


if __name__ == "__main__":
    main()
