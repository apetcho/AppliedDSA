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
        return self._value

    def __add__(self, other: "Integer") -> "Integer":
        """Return sum of two Integer object.
        
        Parameters
        ----------
        other: Integer
        
        Examples
        --------
        >>> a = Integer(3)
        >>> b = Integer(2)
        >>> c = a + b
        >>> repr(c)
        Integer(value=5, valid=True)
        >>> print(c)
        5
        """
        if self._valid and other._valid:
            return Integer(self._value + other._value)
        return Integer(0, False)

    def __neg__(self) -> "Integer":
        """Negate the value of this Integer object value.
        
        Examples
        --------
        >>> a = Integer(3)
        >>> repr(a)
        Integer(value=3, valid=True)
        >>> print(a)
        3
        >>> b = -a
        >>> repr(b)
        Integer(value=-3, valid=True)
        >>> print(b)
        -3
        """
        if self._valid:
            return Integer(-self._value)
        return Integer(0, False)

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
