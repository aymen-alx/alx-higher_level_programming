#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    temp = []
    tList = list(tuple_a)
    tList2 = list(tuple_b)

    if len(tList) == 0:
        tList = [0, 0]
    if len(tList2) == 0:
        tList2 = [0, 0]
    if len(tList) == 1:
        tList.append(0)
    if len(tList2) == 1:
        tList2.append(0)

    temp.append(tList[0] + tList2[0])
    temp.append(tList[1] + tList2[1])
    return tuple(temp)
