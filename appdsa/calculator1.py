"""Simple arithmetic calculator using rational.py module and a binary tree."""
import re
import string
from turtle import left
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


class TermNode:
    """Expression node."""

    def __init__(
        self, term: Rational=None,
        left: "TermNode"=None, right: "TermNode"=None):
        self._term = term
        self._left = left
        self._right = right

    def make_prefix_expr(self) -> str:
        """Return prefix notation form of expression (or term)."""
        if self._term[-1] in string.digits:
            return str(self._term)
        if isinstance(self._left, Rational):
            left = str(self._left)
        else:
            left = self._left.make_prefix_expr()
        if isinstance(self._right, Rational):
            right = str(self._right)
        else:
            right = self._right.make_prefix_expr()

        op = self._term
        retval = (str(op) + "|" + str(left) + "|" + str(right))
        return retval

    def make_infix_expr(self):
        """Return infix notation form of expression (or term)."""
        if self._term[-1] in string.digits:
            return str(self._term)
        if isinstance(self._left, Rational):
            left = str(self._left)
        else:
            left = self._left.make_prefix_expr()
        if isinstance(self._right, Rational):
            right = str(self._right)
        else:
            right = self._right.make_prefix_expr()

        op = self._term
        retval = (str(left) + "|" + str(op) + "|" +  str(right))
        return retval

    def make_postfix_expr(self):
        """Return postfix notation form of expression (or term)."""
        if self._term[-1] in string.digits:
            return str(self._term)
        if isinstance(self._left, Rational):
            left = str(self._left)
        else:
            left = self._left.make_prefix_expr()
        if isinstance(self._right, Rational):
            right = str(self._right)
        else:
            right = self._right.make_prefix_expr()

        op = self._term
        retval = (str(left) + "|" + str(right) + "|" + str(op))
        return retval

    @property
    def term(self):
        return self._term


def simplify_parenthesis(textline: str) -> str:
    """Remove enclosing parenthesis if available."""
    if textline.startswith("(") and textline.endswith(")"):
        textline = textline[1:-1]
    return textline


class ExpressionTree:
    """Binary tree representing an expression."""

    def __init__(self, infix: str):
        self._operators = []
        self._stack = []
        lexer = Lexer()
        tokens = lexer(infix)
        for token in tokens:
            if token[-1] in string.digits:
                self._stack.append(TermNode(token))
                continue
            if token == "(":
                self._operators.append(token)
                continue
            if token == ")":
                while len(self._operators) > 0 and self._operators[-1] != "(":
                    self.new_operation()
            if token in "+-*:/^":
                if token != "^":
                    while (len(self._operators) > 0 and
                        self.priority(
                            self._operators[-1])>=self.priority(token)):
                        self.new_operation()
                self._operators.append(token)
                continue
        while len(self._operators) > 0:
            self.new_operation()
        if len(self._stack) == 1:
            self._root: TermNode = self._stack.pop(-1)

    def new_operation(self):
        top = self._operators.pop(-1)
        right = self._stack.pop(-1)
        left = self._stack.pop(-1)
        node = TermNode(top, left, right)
        self._stack.append(node)

    def priority(self, op: str):
        precedence = 0
        if op == "+" or op == "-":
            precedence = 1
        if op == ":" or op == ":" or op == "/":
            precedence = 2
        if op == "^":
            precedence = 3
        return precedence

    def prefix(self) -> str:
        return self._root.make_prefix_expr()

    def infix(self) -> str:
        return simplify_parenthesis(self._root.make_infix_expr())

    def postfix(self) -> str:
        return self._root.make_postfix_expr()

    def evaluate(self):
        result = []
        tokens = self._root.make_postfix_expr().split("|")
        for token in tokens:
            if token[-1] in string.digits:
                result.append(Rational(int(token)))
                continue
            if token == "+":
                x = result.pop(-1)
                y = result.pop(-1)
                result.append((x+y))
                continue
            if token == "-":
                x = result.pop(-1)
                y = result.pop(-1)
                result.append((x-y))
                continue
            if token == "*":
                x = result.pop(-1)
                y = result.pop(-1)
                result.append((x*y))
                continue
            if token == ":" or token == "/":
                x = result.pop(-1)
                y = result.pop(-1)
                result.append((x/y))
                continue
            if token == "^":
                x = result.pop(-1)
                y = result.pop(-1)
                result.append((x**y))
                continue
        return result.pop(-1)


class Application:

    def __init__(self, expression: str):
        self._expr = expression

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
