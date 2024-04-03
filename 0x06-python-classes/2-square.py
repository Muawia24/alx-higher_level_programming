#!/usr/bin/python3
'''
Square class definition
'''


class Square:

    '''
    Properties of Square

    Attributes:
        size: size of square
    '''
    '''
        creates new instances of square

        Args:
            size: size of square
    '''
    def __init__(self, size=0):

        if type(size) == int:
            self.__size = size

        else:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
