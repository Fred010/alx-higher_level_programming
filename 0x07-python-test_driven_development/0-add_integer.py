#!/usr/bin/python3
"""Define add_integer function"""


def add_integer(a, b=98):
    """Return integer addition of a and b

    Float args are typecasted to ints

    Raises:
        TypeError: if either a or b is a non-integer and non-float"""
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
