#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_dir = sorted(a_dictionary)

    for k, v in sorted(a_dictionary.items()):
        print(k, end=": ")
        print(v)
