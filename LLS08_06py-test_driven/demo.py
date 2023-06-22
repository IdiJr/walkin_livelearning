#!/usr/bin/python3
"""module that contains one add function"""


def add(x, y):
    """Function adds two integers
    Args:
        x (int, float): first argument
        y (int, float): second argument

    Return:
        sum of integers

    Raises:
        TypeError: x or y should be an integer or float

    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be a float or integer")
    if not isinstance(y, (int, float)):
        raise TypeError("y must be a float or integer")
    return (int(x) + int(y))
