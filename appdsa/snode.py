"""Implementation of a singly linked list node."""

class Node:
    """Singly linked list node."""
    __slots__ = "_data", "_next"

    def __init__(self, data=None, next=None):
        self._data = data
        self._next = next

    def __str__(self):
        return str(self._data)

    def __repr__(self):
        return "Node({0}, {1!r})".format(self._data, self._next)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, link):
        self._next = link
