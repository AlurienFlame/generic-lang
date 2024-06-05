from lark import Lark
from transformer import MyTransformer
from argparse import ArgumentParser


def main():
    # Load grammar from file
    grammar = None
    with open("grammar.ebnf") as f:
        grammar = f.read()

    # Create parser and transformer
    parser = Lark(grammar, start="start", parser="lalr")
    transformer = MyTransformer()

    # Load source code from file
    arg_parser = ArgumentParser()
    arg_parser.add_argument("source_file", help="The source file to compile")
    args = arg_parser.parse_args()

    source_code = None
    with open(args.source_file) as f:
        source_code = f.read()

    # Parse and transform the source code
    syntax_tree = parser.parse(source_code)
    # print(syntax_tree.pretty())
    transformer.transform(syntax_tree)
    # print(transformer.symbol_table)


if __name__ == "__main__":
    main()
