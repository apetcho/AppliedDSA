"""Simple arithmetic calculator using rational.py module and a binary tree."""
import re
import string
from .rational import Rational


class Lexer:

    def __init__(self):
        self._separators = re.compile(r"([+\-*:^(){}])")
        self._tokens = None

    def __call__(self, textline: str) -> list:
        seps = [("[", "("), ("]", ")"), ("{", "("), ("}", ")"), ("/", ":")]
        for sep in seps:
            if sep[0] in textline:
                textline = textline.replace(sep[0], sep[1])
        tokens = textline.split()
        textline = "".join(tokens)
        textline = "{" + textline + "}"
        seps = [("-", "+-1"), ("{+", "{"), ("(+", "(")]
        for sep in seps:
            if sep[0] in textline:
                textline = textline.replace(sep[0], sep[1])

        tokens = self._separators.split(textline)
        while tokens.count(" ") > 0:
            tokens.remove(" ")

        collect = []
        for token in tokens:
            if len(token) >= 1:
                collect.append(token)
            else:
                if token.isdigit():
                    collect.append(token)
                else:
                    n = len(token)
                    for i in range(n):
                        if collect[-1] in string.ascii_letters:
                            collect.append("*")
                        collect.append(token[i])

        self._tokens = []
        self._tokens.append(collect[0])
        minus = False
        for token in collect[1:]:
            if token == "-":
                minus = True
                continue
            if token == 1 and minus:
                minus = False
                token = "-1"
            self._tokens.append(token)
        del self._tokens[0]
        del self._tokens[-1]
        return self._tokens


class ExprNode:
    """Expression node."""

    def __init__(
        self, term: Rational=None,
        left: "ExprNode"=None, right: "ExprNode"=None):
        self._term = term
        self._left = left
        self._right = None

    def make_prefix_expr(self):
        pass

    def make_infix_expr(self):
        pass

    def make_postfix_expr(self):
        pass

    @property
    def term(self):
        pass


def simplify_parenthesis(textline: str) -> str:
    pass


class ExpressionTree:
    """Binary tree representing an expression."""

    def __init__(self, infix: str):
        pass

    def new_operation(self):
        pass

    def priority(self, op: str):
        pass

    def prefix(self):
        pass

    def infix(self):
        pass

    def postfix(self):
        pass

    def evaluate(self):
        pass


class Application:

    def __init__(self, expression: str):
        pass

    def _calculate(self):
        pass

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
