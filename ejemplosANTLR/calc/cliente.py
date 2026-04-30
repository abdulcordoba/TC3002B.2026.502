from antlr4 import *
from antlr.ExprLexer import ExprLexer
from antlr.ExprParser import ExprParser
from antlr.ExprListener import ExprListener


class PrefixPrinter(ExprListener):
    # enterXxx = el nodo se visita ANTES que sus hijos → operador primero = prefijo
    def enterInt(self, ctx):
        print(ctx.INT().getText(), end=' ')

    def enterMult(self, ctx):
        print('x', end=' ')

    def enterDiv(self, ctx):
        print('/', end=' ')

    def enterAdd(self, ctx):
        print('+', end=' ')

    def enterSub(self, ctx):
        print('-', end=' ')



class PostfixPrinter(ExprListener):
    # exitXxx = postfijo  →  cambia a enterXxx para prefijo
    def exitInt(self, ctx):
        print(ctx.INT().getText(), end=' ')
    def exitMult(self, ctx):
        print('x', end=' ')
    def exitDiv(self, ctx):
        print('/', end=' ')
    def exitAdd(self, ctx):
        print('+', end=' ')
    def exitSub(self, ctx):
        print('-', end=' ')


def main(argv):
    # input =
    #
    # lexer =
    # stream =
    parser = ExprParser(CommonTokenStream(ExprLexer(FileStream("ejemplo.txt"))))
    tree = parser.prog()

    printer = PostfixPrinter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    print()

if __name__ == '__main__':
    main("")
