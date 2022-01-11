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

    def expr1(self) -> Union[float, int, Rational]:
        """expr1 := expr2 "*" expr2 | expr2 "/" expr2 | expr2 """
        if self.error_exists():
            return 0
        term: Rational = self.expr2()
        while self.is_next("*") or self.is_next("/") or self.is_next(":"):
            self._ch = self.next()
            if self._ch == "*":
                self._ch = self.next()
                term *= self.expr2()
            else:
                if self._ch == "/" or self._ch == ":":
                    self._ch = self.next()
                    term /= self.expr2()
                    if not term.valid:
                        self.error(7)   # division by zero
        return term


    def expr2(self) -> Union[float, int, Rational]:
        """expr2 := '-' expr3 | expr3 """
        if self.error_exists():
            return 0
        negate = False
        while self._ch == "-":
            negate = not negate
            self._ch = self.next()
        term = self.expr3()
        if negate:
            return -term
        return term

    def expr3(self) -> Union[float, int, Rational]:
        """expr3 ::= expr4 "^" expr2 | expr4 """
        if self.error_exists():
            return 0
        term = self.expr4()
        if self.is_next("^"):
            self._ch = self.next()
            self._ch = self.next()
            k: Rational = self.expr2()
            if not k.valid:
                self.error(8)   # invalid exponent
            term = term ** k
        return term

    def expr4(self) -> Union[float, int, Rational]:
        """expr4 ::= <natural> | "(" expr ")" """
        if self.error_exists():
            return 0
        if str.isdigit(self._ch):
            term = self.natural()
            return Rational(int(term))
        if self._ch == "(":
            self._ch = self.next()
            term = self.expr()
            self._ch = self.next()
            if self._ch == ")":
                return term
            else:
                self.error(10)      # missing ")"
        else:
            self.error(9)           # missing "("
        return 0

    def natural(self) -> int:
        """natural ::= "(" '0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9' ")" """
        n = int(self._ch)
        x = self.next_read()
        while str.isdigit(x):
            n = n * 10 + int(x)
            self._ch = self.next()
            x = self.next_read()
        return n


class Application:

    def __init__(self):
        self._expr = None

    def demos(self):
        self._expr = Expression("{ (3 + 4) * 5 ^ (1 + 1) - 7 }")
        print("----------")
        print("Example #1")
        print("----------")
        print(f"Expression ...... : {self._expr}")
        print(f"Result .......... : {self._expr.value()}")

        self._expr = Expression("{ 2 ^ 3 ^ 2 ^ 2 }")
        print("----------")
        print("Example #2")
        print("----------")
        print(f"Expression ...... : {self._expr}")
        print(f"Result .......... : {self._expr.value()}")

        self._expr = Expression("{ ( 9 + 1 ) * ( 7 + 2 * 5 ) }")
        print("----------")
        print("Example #3")
        print("----------")
        print(f"Expression ...... : {self._expr}")
        print(f"Result .......... : {self._expr.value()}")

        self._expr = Expression("{ 3/7 - 2/7 : (5 : 14) }")
        print("----------")
        print("Example #4")
        print("----------")
        print(f"Expression ...... : {self._expr}")
        print(f"Result .......... : {self._expr.value()}")


    def _read_expr(self) -> str:
        print("------------------------------------------------------")
        print("Next calculation (leave empty and press ENTER to quit)")
        print("------------------------------------------------------")
        return input("\x1b[32mcalc2>>\x1b[0m ")

    def _mainloop(self) -> None:
        expr = self._read_expr()
        while len(expr) > 0:
            self._expr = Expression("{" + expr + "}")
            print(f"\x1b[31mresult =\x1b[0m {self._expr.value()}")
            expr = self._read_expr()

    def __call__(self):
        self._mainloop()


def main():
    app = Application()
    app()

# TODO: Check the validity of the code: some hidden bug is in here
