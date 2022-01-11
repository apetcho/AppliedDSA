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
from typing import Union
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

    def noerror(self) -> bool:
        return not self.error_exists()

    def value(self) -> Union[float, int, Rational]:
        self.evaluate()
        return self._value

    def evaluate(self) -> None:
        self._ch = self.next()
        if self._ch == "{":
            self._ch = self.next()
            self._value = self.expr()
            self._ch = self.next()
            if self._ch != "}":
                self.error(2)       # missing one "}"
        else:
            self.error(1)           # missing one "}"

    def next(self) -> str:
        while self._index < self._length:
            token = self._src[self._index]
            self._index += 1
            if str.isspace(token):
                continue
            else:
                return token
        return '\0'

    def next_read(self) -> str:
        while self._index < self._length:
            token = self._src[self._index]
            self._index += 1
            if str.isspace(token):
                self._index += 1
            else:
                return token
        return '\0'

    def is_next(self, token) -> bool:
        if self.next_read() == token:
            return True
        return False

    def expr(self) -> Union[float, int, Rational]:
        """expr ::= expr1 "+" expr1 | expr1 "-" expr1 | expr1 """
        if self.error_exists():
            return 0
        term = self.expr1()
        while self.is_next("+") or self.is_next("-"):
            self._ch = self.next()
            if self._ch == "+":
                self._ch = self.next()
                term += self.expr1()
            else:
                if self._ch == "-":
                    self._ch = self.next()
                    term -= self.expr1()
        return term

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
