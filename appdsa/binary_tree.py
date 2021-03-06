"""An Implementation of Binary Tree."""
from typing import Any


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
                return self._left.search(data)
            else:
                return False
        else:
            if self._right:
                return self._right.search(data)
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
            return self._right.maxval()
        else:
            return self._data

    def minval(self) -> Any:
        if self._left:
            return self._left.minval()
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
                        parent._left = None
                    else:
                        parent._right = None
                else:
                    if self.left is None or self.right is None: # one child
                        if self.left:
                            node = self.left
                        else:
                            node = self.right

                        if parent.left is self:
                            temp = parent.left
                            parent._left = node
                        else:
                            temp = parent.right
                            parent._right = node
                        temp._left = None
                        temp._right = None
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
        container = list()
        self._preorder(container)
        return container

    def display_postorder(self) -> None:
        if self.right:
            self.right.display_postorder()
        print(self.data)
        if self.left:
            self.left.display_postorder()

    def _postorder(self, container:list) -> None:
        if self.right:
            self.right._postorder(container)
        container.append(self.data)
        if self.left:
            self.left._postorder(container)

    def postorder(self) -> list:
        container = list()
        self._postorder(container)
        return container


class BinarySearchTree:
    """Binary Search Tree class."""

    def __init__(self):
        self._root: Node = None

    def display(self) -> None:
        """Print this BST."""
        if self._root:
            self._root.display()
        else:
            print("Empty BST")

    def search(self, data: Any) -> bool:
        """Search data in the BST."""
        if self._root:
            return self._root.search(data)
        else:
            return False

    def insert(self, data: Any) -> None:
        """Insert data into the BST."""
        if self._root:
            self._root.insert(data)
        else:
            self._root = Node(data)

    def delete(self, data: Any) -> None:
        """Delete a data from BST."""
        if self.search(data):
            if self._root.data == data:
                if self._root.left:
                    child = self._root.left
                else:
                    child = self._root.right

                if child is None:
                    self._root = None
                else:
                    if self._root.left:
                        x = child.maxval()
                    else:
                        x = child.minval()
                    self._root.delete(x)
                    self._root.data = x
            else:
                self._root.delete(data)
        else:
            print("Data not in the BST.")

    def display_preorder(self):
        if self._root:
            self._root.display_preorder()
        else:
            print("Empty BST.")

    def display_postorder(self):
        if self._root:
            self._root.display_postorder()
        else:
            print("Empty BST.")

    def preorder(self) -> list:
        if self._root:
            return self._root.preorder()
        else:
            return []

    def postorder(self) -> list:
        if self._root:
            return self._root.postorder()
        else:
            return []

    def num_nodes(self):
        if self._root:
            return self._root.num_nodes()
        else:
            return 0


def _test():
    """Test"""
    import random
    tree = BinarySearchTree()
    for _ in range(10):
        tree.insert(random.randrange(100))

    tree.display()
    print("---", tree.preorder())
    print("---", tree.postorder())
    print(f"{tree.num_nodes()} nodes in the BST")

    end = False
    while not end:
        print("*" * 50)
        print("(a) Add, or (i) Preorder  or (d) Postorder ")
        print("or (r) Remove or (q) Quit?")
        print("*" * 50)
        cmd = input(">> ")[0].lower()
        if cmd == "a" or cmd[0] == "r":
            value = int(input(">> "))
            print("-" * 50)
            if cmd == "a":
                tree.insert(value)
            if cmd == "r":
                tree.delete(value)
        if cmd == "i":
            print(tree.preorder())
        if cmd == "d":
            print(tree.postorder())
        if cmd == "q":
            end = True
        if cmd not in "aidrq":
            print("Valid input commands are: 'a', 'i', 'd', 'r' or 'q'")


if __name__ == "__main__":
    _test()
