"""An implementation of simple arithmetic calculator using a grammar
based on BNF (Backus-Naur-Form) notation.

The grammar is:

expr ::= expr1 "+" expr1 |
         expr1 "-" expr1 |
         expr1

expr1 ::= expr2 "*" expr2 |
          expr2 "/" expr2 |
          expr2

expr2 ::= "-" expr3 |
          expr3

expr3 ::= expr4 "^" expr2 |
          expr4

expr4 ::= <natural> |
         "(" expr ")"

natural ::= ( '0' | '1' | '2' | '3' | '4'| '5' | '6' | '7' | '8' | '9' )*

"""
from .rational import Rational


class Expression:
    """Expression to be evaluated."""

    def __init__(self, src):
        pass

    def __str__(self):
        pass

    __repr__ = __str__

    def error(self):
        pass

    def error_exists(self):
        pass

    def no_error(self):
        pass

    def value(self):
        pass

    def evaluate(self):
        pass

    def next(self):
        pass

    def next_read(self):
        pass

    def is_next(self):
        pass

    def expr(self):
        pass

    def expr1(self):
        pass

    def expr2(self):
        pass

    def expr3(self):
        pass

    def expr4(self):
        pass

    def natural(self):
        pass


class Application:

    def __init__(self):
        self._expr = None

    def demos(self):
        pass

    def _read_expr(self):
        pass

    def _mainloop(self):
        pass

    def __call__(self):
        pass


def main():
    pass
