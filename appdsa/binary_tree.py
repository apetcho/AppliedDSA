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

    def search(self, data: Any) -> bool:
        """Search data in the chain of nodes."""
        if data == self._data:
            return True

        if data < self._data:
            if self._left:
                return self._left.display(data)
            else:
                return False
        else:
            if self._right:
                return self._right.display(data)
            else:
                return False

    def insert(self, data: Any):
        """Insert a data into the tree at appropriate node."""
        if data != self._data:
            if data < self._data:
                if self._left:
                    self._left.insert(data)
                else:
                    self._left = Node(data)
            else:
                if self._right:
                    self._right.insert(data)
                else:
                    self._right = Node(data)
        else:
            print("No duplicate in a binary search tree")

    def maxval(self):
        if self._right:
            return self._right.largest()
        else:
            return self._data

    def minval(self):
        if self._left:
            return self._left.smallest()
        else:
            return self._data

    @property
    def data(self):
        return self._data

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
