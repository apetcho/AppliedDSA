"""Implementation of a simple Stack data structure."""
from .snode import Node


class Stack:
    """Stack data structure."""
    __slots__ = ("_top",)

    def __init__(self):
        self._top: Node = None

    def __str__(self):
        items = []
        node = self._top
        while not(node is None):
            items.append(node.data)
            node = node.next
        return str(items)

    __repr__ = __str__

    def is_empty(self):
        return (self._top is None)

    def push(self, data):
        node = Node(data)
        node.next = self._top
        self._top = node

    def pop(self):
        if self._top is None:
            return None
        node = self._top
        data = node.data
        self._top = node.next
        node = None
        return data


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
