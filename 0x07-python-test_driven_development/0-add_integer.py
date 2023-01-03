#!/usr/bin/python3
"""
This is the 0-add_integer module
It contains 1 function, add_integer(a, b)
"""


def add_integer(a, b=98):
    """
    return addition of two numbers without decimal point
    """
    if type(a) != float and type(a) != int:
        raise TypeError('a must be an integer')
    if type(b) != float and type(b) != int:
        raise TypeError('b must be an integer')

    return int(a) + int(b)
