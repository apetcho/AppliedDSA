"""Implementation of stack data structure using a singly linked list."""
from .snode import Node

class Queue:
    """Queue Data Structure."""

    def __init__(self):
        self._first : Node = None
        self._last : Node = None

    def __str__(self) -> str:
        items = []
        node = self._first
        while not (node is None):
            items.append(node.data)
            node = node.next
        return str(items)

    __repr__ = __str__

    def is_empty(self):
        return (self._first is None)

    def enqueue(self, data):
        node = Node(data)
        if self._first is None:
            self._first = node
        else:
            self._last.next = node
        self._last = node

    def dequeue(self):
        if self._first is None:
            return None
        node = self._first
        data = node.data
        self._first = node.next
        node = None
        return data


if __name__ == "__main__":
    q = Queue()
    q.enqueue("GNU")
    q.enqueue("is")
    q.enqueue("not")
    q.enqueue("UNIX")
    print(q)
    while not q.is_empty():
        print(q.dequeue())
