#!/usr/bin/python3

'''Square class definition'''


class Square:
    '''     properties of square

            attributes:
                size: size of square
    '''

    def __init__(self, size=0, position=(0, 0)):
        '''
        instansiate an instance of square

        Args:
            size: size of square
            position: cordinates
        '''
        self.__size = size
        self.__position = position

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
        if type(value) != int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Returns the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Property setter for position.

        Args:
            value (tuple): position of the square.

        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """

        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(i) != int for i in value) or any(j < 0 for j in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        '''
         public method to calc area of square

          Return: the area of a square
        '''
        return self.__size * self.__size

    def my_print(self):

        """prints in stdout the square with the character #
        """

        if self.__size == 0:
            print()
        for n in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
