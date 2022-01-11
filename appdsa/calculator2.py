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
        self._src = src
        self._length = len(src)
        self._index = 0
        self._error = 0
        self._value = 0

    def __str__(self) -> str:
        retval = ""
        for ch in self._src:
            if not str.isspace(ch):
                retval += ch
        return retval

    __repr__ = __str__

    def error(self, err: int) -> None:
        if self._error == 0:
            self._error = err

    def error_exists(self) -> bool:
        if self._error == 0:
            return False
        return True

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
