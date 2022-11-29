#!/usr/bin/python3
def remove_char_at(str, n):
    reserve = ""

    for i in range(len(str)):
        if i != n:
            reserve += str[i]
    return (reserve)
