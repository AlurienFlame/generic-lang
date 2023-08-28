from lark import Transformer


class MyTransformer(Transformer):
    # Create a transformer to evaluate the syntax tree
    symbol_table = {}

    # NULLARY NODES
    def start(self, args):
        return args[0]

    def num(self, args):
        return float(args[0])

    def expr(self, args):
        return args[0]

    def term(self, args):
        return args[0]

    def factor(self, args):
        return args[0]

    # UNARY NODES
    def neg(self, args):
        return -args[0]

    def var(self, args):
        return self.symbol_table[args[0]]

    def functionDefinition(self, args):
        self.symbol_table[args[0]] = args[1]
        return None

    # BINARY NODES
    def add(self, args):
        return args[0] + args[1]

    def sub(self, args):
        return args[0] - args[1]

    def mul(self, args):
        return args[0] * args[1]

    def div(self, args):
        return args[0] / args[1]

    def assign(self, args):
        self.symbol_table[args[0]] = args[1]
        return args[1]
