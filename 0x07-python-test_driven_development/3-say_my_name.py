#!/usr/bin/python3
"""
This is the 3-say_my_name module
It contains 1 function, say_my_name(first_name, last_name=""):
"""


def say_my_name(first_name, last_name=""):
    """
        Function display full name or if last name is't avariable
        just display first name only

        Args:
            first_name (str): First name
            last_name (str): Last name
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    elif type(last_name) != str:
        raise TypeError("last_name must be a string")

    print('My name is {} {}'.format(first_name, last_name))
