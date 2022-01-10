"""Utilities for computing with numbers."""

def num_truncate(value: float) -> int:
    """Truncate a floating point value.
    
    Parameters
    ----------
    value: float
    
    Examples
    --------
    >>> num_truncate(6.2)
    6
    >>> num_truncate(-9.1)
    -9
    """
    return int(value)


def num_floor(value: float) -> int:
    """Return the floor approximation of value
    
    Paramters
    ---------
    value: float
    
    Examples
    --------
    >>> num_floor(3.1)
    3
    >>> num_floor(-3.1)
    -4
    """
    value = (value - 1) if value < 0 else value
    return int(value)


def num_fractional_part(value: float) -> float:
    """Return the fractional part of a floating point value in mathematical
    sens.
    
    Parameters
    ----------
    value: float
    
    Examples
    --------
    >>> num_fractional_part(-2.1)
    0.9
    >>> num_fractional_part(2.1)
    0.1
    """
    return value - num_floor(value)
