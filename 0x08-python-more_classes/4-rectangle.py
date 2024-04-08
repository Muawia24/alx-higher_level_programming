#!/usr/bin/python3
""" Rectangle class definition """


class Rectangle:
    """ Rectangle methods """

    def __init__(self, width=0, height=0):
        """ sets two attributes """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width getter function """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter method """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height getter method """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter method """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """ returns the rectangle area """

        return self.__width * self.__height

    def perimeter(self):
        """  returns the rectangle perimeter """

        if self.__width == 0 or self.__height == 0:
            return 0

        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """
        print the rectangle with the character #
        """

        if self.__width == 0 or self.height == 0:
            return ""
        s = []
        for i in range(self.__height):
            s.append('#' * self.__width)

        return "\n".join(s)

    def __repr__(self):
        """
        return a string representation of the rectangle
        """

        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
