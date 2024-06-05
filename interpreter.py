from lark import Tree
from lark.visitors import Interpreter

class GlaException(Exception):
    pass

class Undefined:
    def __repr__(self):
        return "Undefined"
undefined = Undefined()

class Lambda:
    def __init__(self, parameters, body):
        self.parameters = parameters
        self.body = body
    def __repr__(self):
        return f"Lambda({len(self.parameters)})[{len(self.body.children)}]"

class SymbolTable:
    scopes = []
    def enter_scope(self):
        self.scopes.append({})
    def exit_scope(self):
        self.scopes.pop()
    def __getitem__(self, key):
        for scope in reversed(self.scopes):
            if key in scope:
                return scope[key]
        print(f"Failed to find {key} in symbol table")
        return undefined
    def __setitem__(self, key, value):
        self.scopes[-1][key] = value
        # print(f"{key} = {value}")
    def __repr__(self):
        result = ""
        for i in range(len(self.scopes)):
            result += f"Scope {i}: {self.scopes[i]}\n"
        return result

class GlaInterpreter(Interpreter):
    # Create a transformer to evaluate the syntax tree
    symbol_table = SymbolTable()

    def logsymtab(self, args):
        print(self.symbol_table)

    def program(self, args):
        self.symbol_table.enter_scope()
        for statement in args.children:
            self.visit(statement)
        self.symbol_table.exit_scope()

    # Statements
    def conditional(self, args: Tree):
        # if
        if self.visit(args.children[0]):
            self.visit(args.children[1])
            return

        # else if
        for i in range(2, len(args.children) - 2, 2):
            if self.visit(args.children[i]):
                self.visit(args.children[i+1])
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
        # print(f"{token}++")

    def call(self, args):
        # e1 = id, e2..n = arguments
        # print(f"Calling {args.children[0]}")
        lam = self.visit(args.children[0])
        if isinstance(lam, Undefined):
            raise GlaException(f"Tried to call undefined function")
        self.symbol_table.enter_scope()
        for i in range(len(lam.parameters)):
            self.symbol_table[lam.parameters[i].value] = self.visit(args.children[i + 1])
        self.visit(lam.body)
        self.symbol_table.exit_scope()

    # Expressions
    def lam(self, args):
        # e1..n-1 = parameters, en = body
        lam = Lambda(args.children[:-1], args.children[-1])
        # print(f"Defining lambda {lam}")
        return lam

    def assign(self, args):
        identifier = args.children[0].value
        value = self.visit(args.children[1])
        self.symbol_table[identifier] = value
        # print(f"{identifier} = {value}")

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
        # print(f"Looking up {args.children[0]}")
        return self.symbol_table[args.children[0].value]

    def string(self, args):
        return str(args.children[0])

    def log(self, args):
        print(self.visit(args.children[0]))

    # BINARY NODES
    def add(self, args):
        return self.visit(args.children[0]) + self.visit(args.children[1])

    def sub(self, args):
        return self.visit(args.children[0]) - self.visit(args.children[1])

    def mul(self, args):
        return self.visit(args.children[0]) * self.visit(args.children[1])

    def div(self, args):
        return self.visit(args.children[0]) / self.visit(args.children[1])

    def mod(self, args):
        return self.visit(args.children[0]) % self.visit(args.children[1])

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
