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
        pass

    @property
    def denominator(self):
        pass

    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        pass

    def __float__(self) -> float:
        pass

    def __add__(self, other: "Rational") -> "Rational":
        pass

    def __neg__(self) -> "Rational":
        pass

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
