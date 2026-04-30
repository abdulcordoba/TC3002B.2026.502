from antlr4 import *
from antlr.ExprLexer import ExprLexer
from antlr.ExprParser import ExprParser
from antlr.ExprListener import ExprListener

r = []

class Interprete(ExprListener):
    def exitInt(self, ctx):
        r.append(int(ctx.INT().getText()))

    def exitNeg(self, ctx):
        r.append(-r.pop())

    def exitMult(self, ctx):
        b, a = r.pop(), r.pop()
        r.append(a * b)

    def exitDiv(self, ctx):
        b, a = r.pop(), r.pop()
        r.append(a / b)

    def exitMod(self, ctx):
        b, a = r.pop(), r.pop()
        r.append(a % b)

    def exitAdd(self, ctx):
        b, a = r.pop(), r.pop()
        r.append(a + b)

    def exitSub(self, ctx):
        b, a = r.pop(), r.pop()
        r.append(a - b)

def main(argv):
    input = FileStream("ejemplo.txt")

    lexer = ExprLexer(input)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()

    interprete = Interprete()
    walker = ParseTreeWalker()
    walker.walk(interprete, tree)
    print(r)

if __name__ == '__main__':
    main("")
