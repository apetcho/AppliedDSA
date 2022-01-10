"""Module containing a Rational class representing rational numbers."""
from __future__ import division
from typing import Union
from integer import Integer as Integer_t


def check_int(value: int):
    pass


class Rational:
    """Rational number class."""

    def __init__(self, num=0, den=1, valid=True):
        pass

    @property
    def valid(self):
        pass

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
