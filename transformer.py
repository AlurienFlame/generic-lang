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
        return self.symbol_table[args[0].value]

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
        self.symbol_table[args[0].value] = args[1]
        return args[1]

    # Boolean operators
    def eq(self, args):
        return args[0] == args[1]

    def neq(self, args):
        return args[0] != args[1]

    def lt(self, args):
        return args[0] < args[1]

    def gt(self, args):
        return args[0] > args[1]

    def leq(self, args):
        return args[0] <= args[1]

    def geq(self, args):
        return args[0] >= args[1]

    def land(self, args):
        return args[0] and args[1]

    def lor(self, args):
        return args[0] or args[1]

    def lnot(self, args):
        return not args[0]

    def true(self, args):
        return True

    def false(self, args):
        return False
