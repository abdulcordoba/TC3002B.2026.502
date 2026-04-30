from antlr4 import *
from antlr.ExprLexer import ExprLexer
from antlr.ExprParser import ExprParser
from antlr.ExprListener import ExprListener

regs = []
temp = [0]

def new_temp():
    reg = f"$t{temp[0]}"
    temp[0] += 1
    return reg


class MIPSGenerator(ExprListener):
    def exitInt(self, ctx):
        reg = new_temp()
        print(f"li {reg}, {ctx.INT().getText()}")
        regs.append(reg)

    def exitAdd(self, ctx):
        b, a = regs.pop(), regs.pop()
        reg = new_temp()
        print(f"add {reg}, {a}, {b}")
        regs.append(reg)

    def exitSub(self, ctx):
        b, a = regs.pop(), regs.pop()
        reg = new_temp()
        print(f"sub {reg}, {a}, {b}")
        regs.append(reg)

    def exitMult(self, ctx):
        b, a = regs.pop(), regs.pop()
        reg = new_temp()
        print(f"mul {reg}, {a}, {b}")
        regs.append(reg)

    def exitDiv(self, ctx):
        b, a = regs.pop(), regs.pop()
        reg = new_temp()
        print(f"div {a}, {b}")
        print(f"mflo {reg}")
        regs.append(reg)

    def exitGroup(self, ctx):
        pass  # el valor ya está en la pila, no hay que hacer nada


def main(argv):
    input = FileStream("ejemplo.txt")

    lexer = ExprLexer(input)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()

    walker = ParseTreeWalker()
    walker.walk(MIPSGenerator(), tree)

if __name__ == '__main__':
    main("")
