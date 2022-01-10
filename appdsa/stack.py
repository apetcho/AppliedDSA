"""Implementation of a simple Stack data structure."""
from .snode import Node


class Stack:
    """Stack data structure."""

    def __init__(self):
        self._top: Node = None

    def __str__(self):
        pass

    __repr__ = __str__

    def is_empty(self):
        pass

    def push(self, data):
        pass

    def pop(self):
        pass


def _test():
    stk = Stack()
    stk.push("GNU")
    stk.push("is")
    stk.push("not")
    stk.push("UNIX")
    print(stk)
    while not stk.is_empty():
        print(stk.pop())


if __name__ == "__main__":
    _test()
