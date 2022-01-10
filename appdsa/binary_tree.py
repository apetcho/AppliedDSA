"""An Implementation of Binary Tree."""
from typing import Any

class Node:
    """Binary Tree node."""
    __slots__ = "_data", "_left", "_right"

    def __init__(self, data: Any, left: "Node"=None, right: "Node"=None):
        self._data = data
        self._left = left
        self._right = right

    def display(self, indent=0):
        """Print this node and its children."""
        if self._right:
            self._right.display(indent+3)
        print(f"{(' '*indent)} {self._data}")
        if self._left:
            self._left.display(indent+3)

    def search(self, data: Any):
        pass

    def insert(self, data: Any):
        pass

    def largest(self):
        pass

    def smallest(self):
        pass

    @property
    def data(self):
        pass

    @property
    def left(self):
        pass

    @property
    def right(self):
        pass

    def num_nodes(self):
        pass

    def search_parent(self, data):
        pass

    def delete_node(self, data, parent):
        pass

    def delete(self, data):
        pass

    def display_preorder(self):
        pass

    def _preorder(self, container):
        pass

    def preorder(self):
        pass

    def _postorder(self, container):
        pass

    def postorder(self):
        pass


class BinarySearchTree:
    """Binary Search Tree class."""

    def __init__(self):
        pass

    def display(self):
        pass

    def search(self, data):
        pass

    def insert(self, data):
        pass

    def delete(self, data):
        pass

    def preorder(self):
        pass

    def display_preorder(self):
        pass

    def postorder(self):
        pass

    def display_postorder(self):
        pass

    def num_nodes(self):
        pass


def _test():
    pass


if __name__ == "__main__":
    _test()