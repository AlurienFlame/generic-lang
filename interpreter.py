from lark import Tree
from lark.visitors import Interpreter

def log(st):
    if True: # Logging enabled
        print(st)

class GlaException(Exception):
    pass

class GlaInterpreter(Interpreter):
    # Create a transformer to evaluate the syntax tree
    symbol_table = {}

    # Statements
    def conditional(self, args: Tree):
        # if
        if args.children[0]:
            self.visit(args.children[0])
            return

        # else if
        for i in range(len(args.children[1:-1])):
            if args.children[i]:
                self.visit(args.children[i])
                return

        # else
        self.visit(args.children[-1])

    def pred(self, args):
        # e1 = pred, e2 = body
        if self.visit(args.children[0]):
            self.visit(args.children[1])
            return True
        return False

    def while_loop(self, args):
        while self.visit(args.children[0]):
            self.visit(args.children[1])

    def increment(self, args):
        token = args.children[0].value
        self.symbol_table[token] += 1
        log(f"{token} = {self.symbol_table[token]}")

    # NULLARY NODES
    def start(self, args):
        return self.visit(args.children[0])

    def num(self, args):
        return float(args.children[0])

    def expr(self, args):
        return self.visit(args.children[0])

    def term(self, args):
        return self.visit(args.children[0])

    def factor(self, args):
        return self.visit(args.children[0])

    # UNARY NODES
    def neg(self, args):
        return -self.visit(args.children[0])

    def var(self, args):
        if args.children[0].value not in self.symbol_table:
            raise GlaException(f"Variable {args.children[0].value} not defined")
        return self.symbol_table[args.children[0].value]

    # BINARY NODES
    def add(self, args):
        return self.visit(args.children[0]) + self.visit(args.children[1])

    def sub(self, args):
        return self.visit(args.children[0]) - self.visit(args.children[1])

    def mul(self, args):
        return self.visit(args.children[0]) * self.visit(args.children[1])

    def div(self, args):
        return self.visit(args.children[0]) / self.visit(args.children[1])

    def assign(self, args):
        token = args.children[0].value
        value = self.visit(args.children[1])
        self.symbol_table[token] = value
        log(f"{token} = {value}")
        return self.visit(args.children[1])

    # Boolean operators
    def eq(self, args):
        return self.visit(args.children[0]) == self.visit(args.children[1])

    def neq(self, args):
        return self.visit(args.children[0]) != self.visit(args.children[1])

    def lt(self, args):
        return self.visit(args.children[0]) < self.visit(args.children[1])

    def gt(self, args):
        return self.visit(args.children[0]) > self.visit(args.children[1])

    def leq(self, args):
        return self.visit(args.children[0]) <= self.visit(args.children[1])

    def geq(self, args):
        return self.visit(args.children[0]) >= self.visit(args.children[1])

    def land(self, args):
        return self.visit(args.children[0]) and self.visit(args.children[1])

    def lor(self, args):
        return self.visit(args.children[0]) or self.visit(args.children[1])

    def lnot(self, args):
        return not self.visit(args.children[0])

    def true(self, args):
        return True

    def false(self, args):
        return False
