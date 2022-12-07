#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    new = 0
    key = None
    for k, v in a_dictionary.items():
        if new < v:
            new = v
            key = k
    return key
