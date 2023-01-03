#!/usr/bin/python3
"""
This is the 4-print_square module.
It contains 1 function: print_square(size):
"""


def print_square(size):
    """
    """
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    elif type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print('#', end="")
        print("")
