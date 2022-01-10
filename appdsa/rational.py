"""Module containing a Rational class representing rational numbers."""
from __future__ import division
from typing import Union
from .integer import Integer as Integer_t 


def check_int(value: int) -> bool:
    """Check whether value can be written as 2^p * 5^q where p and q are
    natural numbers."""
    if value == 1:
        return True
    else:
        if value % 2 == 0:
            return check_int(value//2)
        if value % 5 == 0:
            return check_int(value//5)
    return False


class Rational:
    """Rational number class."""

    def __init__(self, num=0, den=1, valid=True):
        valid = valid and ((type(num)==int) or isinstance(num, Integer_t))
        valid = valid and ((type(den)==int) or isinstance(den, Integer_t))
        if valid:
            if type(num) == int:
                num = Integer_t(num)
            if type(den) == int:
                den = Integer_t(den)

        valid = valid and num.valid and den.valid
        self._valid = valid and (den.value != 0)

        if self._valid:
            if den.value < 0:
                num, den = -num, -den
            d = Integer_t.gcd(num, den)
            self._num = num / d
            self._den = den / d
        else:
            self._num = Integer_t(0)
            self._den = Integer_t(1)

    @property
    def valid(self):
        return self._valid

    @property
    def numerator(self):
        return self._num

    @property
    def denominator(self):
        return self._den

    def __str__(self) -> str:
        """Return the string representation of Rational object."""
        if self.valid:
            if self.denominator.value == 1:
                return str(self.numerator)
            if check_int(self.denominator.value):
                return str(self.__float__())
            else:
                return str(self.numerator) + "/" + str(self.denominator)
        return "---[Invalid Rational Object]---"

    def __repr__(self) -> str:
        retval = ""
        if self.valid:
            retval = ("Rational(num={0}, den={1}, valid=True)".format(
                self.numerator, self.denominator
            ))
        else:
            retval = ("Rational(num={0}, den={1}, valid=False)".format(
                self.numerator, self.denominator
            ))
        return retval

    def __float__(self) -> float:
        """Return the representation of Ration in floating point form."""
        if self.valid:
            x, y = self.numerator.value, self.denominator.value
            return float(x)/float(y)
        else:
            return float(0)

    def __add__(self, other: "Rational") -> "Rational":
        """Overload binaray operation (+) for Rational objects.
        
        Parameters
        ----------
        other: Rational
        
        Examples
        --------
        >>> x = Rational(3, 7)
        >>> y = Rational(9, 11)
        >>> z = x + y
        >>> print(f"({x!s}, {y!s}, {z!s})")
        (3/7, 9/11, 96/77)
        >>> x = Rational(3, 4)
        >>> y = Rational(9, 8)
        >>> z = x + y
        >>> print(f"({x!s}, {y!s}, {z!s})")
        (0.75, 1.125, 1.875)
        """
        if self.valid and other.valid:
            a, b = self.numerator, self.denominator
            p, q = other.numerator, other.denominator
            num = a*q + b*p
            den = b*q
            return Rational(num, den)
        else:
            Rational(0, 1, False)

    def __neg__(self) -> "Rational":
        """Overload the negation unary operator.
        
        Examples
        --------
        >>> x = Rational(3, 4)
        >>> print(x)
        0.75
        >>> x = -x
        >>> print(x)
        -0.75
        >>> x = Rational(4, 3)
        >>> print(x)
        4/3
        >>> x = -x
        >>> print(x)
        -4/3
        """
        if self.valid:
            num, den = self.numerator, self.denominator
            return Rational(-num, den)
        else:
            Rational(0, 1, False)

    def __sub__(self, other: "Rational") -> "Rational":
        pass

    def __mul__(self, other: "Rational") -> "Rational":
        pass

    def __truediv__(self, other: "Rational") -> "Rational":
        pass

    __div__ = __truediv__

    def __pow__(self, other: "Rational") -> "Rational":
        pass

    def __eq__(self, other: "Rational") -> "Rational":
        pass

    def __lt__(self, other: "Rational") -> "Rational":
        pass

    def __gt__(self, other: "Rational") -> "Rational":
        pass

    def __le__(self, other: "Rational") -> "Rational":
        pass

    def __ge__(self, other: "Rational") -> "Rational":
        pass
