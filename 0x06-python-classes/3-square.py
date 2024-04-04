#!/usr/bin/python3
'''Square class definition'''


class Square:
    '''     properties of square.

            attributes:
                size: size of square.
    '''

    def __init__(self, size=0):
        '''
        instansiate an instance of square.

        Args:
            size: size of square.
        '''
        if type(size) == int:
            self.__size = size

        else:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''
        Public method to calc area of square.

        Return: the area of a square.
        '''
        return self.__size ** 2
