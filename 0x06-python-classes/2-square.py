#!/usr/bin/python3
'''defines class square'''


class Square:

    ''' create private instance attribute: size'''
    def __init__(self, size=0):
        '''Size validation'''
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
