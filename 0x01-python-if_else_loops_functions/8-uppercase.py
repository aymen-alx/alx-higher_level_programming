#!/usr/bin/python3
# sample best
def uppercase(str):
    for i in range(len(str)):
        temp = ord(str[i])

        if temp >= 97 and temp <= 122:
            temp -= 32
        print("{}".format(chr(temp)), end="")
    print()
