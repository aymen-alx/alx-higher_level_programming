#!/usr/bin/python3

def multiple_returns(sentence):

    if len(sentence) > 0:
        length = len(sentence)
        firstChar = sentence[0]
    else:
        length = 0
        firstChar = None

    return (length, firstChar)
