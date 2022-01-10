"""An Implementation of Binary Tree."""
from typing import Any

from matplotlib import container

class Node:
    """Binary Tree node."""
    __slots__ = "_data", "_left", "_right"

    def __init__(self, data: Any, left: "Node"=None, right: "Node"=None):
        self._data = data
        self._left = left
        self._right = right

    def display(self, indent=0) -> None:
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

    def insert(self, data: Any) -> None:
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

    def maxval(self) -> Any:
        if self._right:
            return self._right.largest()
        else:
            return self._data

    def minval(self) -> Any:
        if self._left:
            return self._left.smallest()
        else:
            return self._data

    @property
    def data(self) -> Any:
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def left(self) -> "Node":
        return self._left

    @property
    def right(self) -> "Node":
        return self._right

    def num_nodes(self) -> int:
        """Return the number of node in the BST."""
        n = 1
        if self._left:
            n = n + self._left.num_nodes()
        if self._right:
            n = n + self._right.num_nodes()
        return n

    def search_parent(self, data) -> "Node":
        if data == self._data: # root node
            return None

        if data < self._data:   # Maybe in the left subtree
            if self._left.data == data:
                return self     # this node is the parent node
            else:
                return self._left.search_parent(data)   # continue the search
        else:                   # Maybe in the right subtree
            if self._right.data == data:
                return self     # this node is the parent node
            else:
                return self._right.search_parent(data)  # continue the search

    def delete_node(self, data, parent: "Node"):
        if data < self.data:
            self.left.delete_node(data, parent)
        else:
            if data > self.data:
                self.right.delete_node(data, parent)
            else:
                if self.left is None and self.right is None: # node children
                    if parent.left is self:
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    if self.left is None or self.right is None: # one child
                        if self.left:
                            node = self.left
                        else:
                            node = self.right

                        if parent.left is self:
                            temp = parent.left
                            parent.left = node
                        else:
                            temp = parent.right
                            parent.left = node
                        temp.left = None
                        temp.right = None
                    else:   # two children
                        if self.left.num_nodes() > self.right.num_nodes():
                            x = self.left.maxval()
                        else:
                            x = self.right.minval()
                        self.delete(x)
                        self.data = x 

    def delete(self, data):
        """Delete a data from the BST."""
        parent = self.search_parent(data)
        self.delete_node(data, parent)

    def display_preorder(self):
        if self.left:
            self.left.display_preorder()
        print(self.data)
        if self.right:
            self.right.display_preorder()

    def _preorder(self, container:list) -> None:
        if self.left:
            self.left._preorder(container)
        container.append(self.data)
        if self.right:
            self.right._preorder(container)

    def preorder(self) -> list:
        """ container = list()
        self._preorder(container)
        return container """

    def display_postorder(self):
        """ if self.right:
            self.right.display_postorder()
        print(self.data)
        if self.left:
            self.right.display_postorder() """

    def _postorder(self, container:list):
        """ if self.right:
            self.right._postorder(container)
        container.append(self.data)
        if self.left:
            self.left._postorder(container) """

    def postorder(self):
        """ container = list()
        self._postorder(container)
        return container """


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
