from lark import Transformer


class MyTransformer(Transformer): # TODO: Inherit fron Interpreter instead to evaluate top-down
    # Create a transformer to evaluate the syntax tree
    symbol_table = {}

    # Statements
    def conditional(self, args):
        # e1 = pred, e2...n-1 = else ifs, e_n = else
        if not args[0]:
            for i in range(1, len(args) - 1, 2):
                args[i]
            return args[-1]
        pass

    def pred(self, args):
        # e1 = pred, e2 = body
        if args[0]:
            args[1]
            return True
        return False

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
        print(f"Assigning {args[1]} to {args[0].value}")
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
