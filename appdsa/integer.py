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

    def __sub__(self, other: "Integer") -> "Integer":
        """Oveload arithmetic substraction binary operation on two Integers.

        Parameters
        ----------
        other: Integer

        Examples
        --------
        >>> a = Integer(5)
        >>> print(a)
        5
        >>> b = Integer(3)
        >>> print(b)
        3
        >>> c = a - b
        >>> print(c)
        2
        >>> d = b - a
        >>> print(d)
        -2
        """
        return self.__add__(other.__neg__())

    def __mul__(self, other: "Integer") -> "Integer":
        """Overload the arithmetic multiplication binary operation for 
        Integers.

        Parameters
        ----------
        other: Integer

        Examples
        --------
        >>> a = Integer(5)
        >>> b = Integer(3)
        >>> print(f"a={a!s}, b={b!s}")
        a=5, b=3
        >>> c = a * b
        >>> print(c)
        15
        """
        if self.valid and other.valid:
            return Integer(self.value * other.value)
        return Integer(0, False)

    def __div__(self, other: "Integer") -> "Integer":
        """Overload arithmetic division (/) for Integer objects.
        
        Paramters
        ---------
        other: Integer
        
        Examples
        --------
        >>> a = Integer(7)
        >>> b = Integer(3)
        >>> c = a / b
        >>> print(c)
        2
        >>> d = b / a
        >>> print(d)
        0
        """
        if not(self.valid and other.valid):
            return Integer(0, False)
        if other.value == 0:
            return Integer(0, False)
        if self.value < other.value:
            return Integer(0)
        return Integer(int(self.value / other.value))

    __truediv__ = __div__
    __floordiv__ = __div__

    def __pow__(self, other):
        pass

    @staticmethod
    def gcd(a: "Integer", b: "Integer") -> "Integer":
        pass
