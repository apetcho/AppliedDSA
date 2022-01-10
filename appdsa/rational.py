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
