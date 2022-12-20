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

    @property
    def size(self):
        '''finds size'''
        return self.__size

    @size.setter
    def size(self, value):
        'validates size is an integer that is greater than zero'''
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

        '''calculate square area'''
    def area(self):
        return self.__size * self.__size
