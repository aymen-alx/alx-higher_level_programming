#!/usr/bin/python3
'''defines class square'''


class Square:

    ''' create private instance attribute: size'''
    def __init__(self, size=0, position=(0, 0)):
        '''Size validation'''
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
        self.position = position

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

    @property
    def position(self):
        '''finds position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''
        sets position

        Args:
            value: position of the square
        '''
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        '''prints square with character'''
        if self.__size == 0:
            print("")
            return
        for i in range(self.position[1]):
            print("")
        for i in range(self.__size):
            print("{}{}".format(" " * self.__position[0], "#" * self.__size))
