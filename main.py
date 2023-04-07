from lark import Lark
from transformer import MyTransformer

def main():
    # Load grammar from file
    grammar = None
    with open('grammar.ebnf') as f:
        grammar = f.read()

    # Create parser and transformer
    parser = Lark(grammar, start='start', parser='lalr')
    transformer = MyTransformer()

    # Main loop
    while True:
        expression = input("> ")
        syntax_tree = parser.parse(expression)
        print(syntax_tree.pretty())
        result = transformer.transform(syntax_tree)
        print(result)


if __name__ == '__main__':
    main()
