#!/usr/bin/python3

'''Square class definition'''


class Square:
    '''     properties of square

            attributes:
                size: size of square
    '''

    def __init__(self, size=0):
        '''
        instansiate an instance of square

        Args:
            size: size of square
        '''
        if type(size) == int:
            self.__size = size

    @property
    def size(self):
        """Returns the size of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter for size.

        Args:
            value (int): size of a square (1 side).

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
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
        return self.__size ** 2

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()
