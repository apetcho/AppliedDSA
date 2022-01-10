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
