#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return None

    length = len(my_list)
    i = 1
    while i <= length:
        idx = i * -1
        print("{:d}".format(my_list[idx]))
        i += 1
