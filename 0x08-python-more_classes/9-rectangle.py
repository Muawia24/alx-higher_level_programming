#!/usr/bin/python3
""" Rectangle class definition """


class Rectangle:
    """ Rectangle methods """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ sets two attributes """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
            s.append(str(self.print_symbol) * self.__width)

        return "\n".join(s)

    def __repr__(self):
        """
        return a string representation of the rectangle
        """
        wid = self.__width
        hi = self.__height

        return "Rectangle(" + str(wid) + ", " + str(hi) + ")"

    def __del__(self):
        """
        Print a message when an instance is deleted
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        eturns a new Rectangle instance with width == height == size
        """

        return cls(size, size)
