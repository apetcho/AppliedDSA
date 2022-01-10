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

    def is_empty(self):
        return (self._first is None)

    def enqueue(self, data):
        pass

    def dequeue(self):
        pass
