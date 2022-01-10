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
        """Return a string representation of Integer object"""
        if self._valid:
            return f"{self._value}"
        return "--[Invalid integer]--"

    def __repr__(self) -> str:
        """Return a repr string form of Integer object."""
        retval = None
        if self._valid:
            retval = rf"Integer(value={self._value}, valid=True)"
        else:
            retval = r"Integer(value=0, valid=False)"
        return retval

    @property
    def valid(self):
        return self._valid

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
