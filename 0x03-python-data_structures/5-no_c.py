#!/usr/bin/python3

# c(99) C(67)
def no_c(my_string):
    temp = ""
    for char in my_string:
        if ord(char) == 99:
            pass
        elif ord(char) == 67:
            pass
        else:
            temp += char
    return temp
