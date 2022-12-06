#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    copyList = my_list.copy()
    length = len(my_list) - 1

    if idx > length:
        return copyList
    elif idx < 0:
        return copyList
    else:
        copyList[idx] = element
        return copyList
