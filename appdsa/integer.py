"""Module containing a class Integer representation of integer numbers.

The Integer class emulate the integers by implementing basic arithmetic
operations and a static method for computing the gcd of two Integers.
"""
from __future__ import division

def gcd(a: int, b: int) -> int:
    pass


class Integer:
    """Integer class."""

    def __init__(self, value: int=0, valid=True):
        self._valid = valid
        self._value = value if self._valid else 0

    def __str__(self) -> str:
        pass

    @property
    def valid(self):
        pass

    @property
    def value(self):
        pass

    def __add__(self, other) -> "Integer":
        pass

    def __neg__(self) -> "Integer":
        pass

    def __sub__(self, other) -> "Integer":
        pass

    def __mul__(self, other) -> "Integer":
        pass

    def __truediv__(self, other) -> "Integer":
        pass

    __div__ = __truediv__
    __floordiv__ = __truediv__

    def __pow__(self, other):
        pass

    @staticmethod
    def gcd(a: "Integer", b: "Integer") -> "Integer":
        pass
