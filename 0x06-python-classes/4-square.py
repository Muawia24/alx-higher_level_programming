#!/usr/bin/python3

'''Square class definition'''


class Square:
    '''     properties of square

            attributes:
                size: size of square
    '''

    def __init__(self, size):
        '''
        instansiate an instance of square

        Args:
            size: size of square
        '''
        if type(size) == int:
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) == int:
            self.__size = value
        else:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''
         public method to calc area of square

          Return: the area of a square
        '''
        return self.__size * self.__size