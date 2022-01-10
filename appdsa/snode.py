"""Implementation of a singly linked list node."""

class Node:
    """Singly linked list node."""

    def __init__(self, data=None, next=None):
        self._data = data
        self._next = next

    def __str__(self):
        return str(self._data)

    def __repr__(self):
        return "Node({0}, {1!s})".format(self._data, self._next)

    @property
    def data(self):
        pass

    @data.setter
    def data(self, value):
        pass

    @property
    def next(self):
        pass

    @next.setter
    def next(self, link):
        pass
