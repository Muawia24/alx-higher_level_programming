#!/usr/bin/python3
""" Rectangle module """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class attributes """
    def __init__(self, width, height):
        """ Instantiation method """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Return the area of Rectangle """
        return self.__height * self.__width

    def __str__(self):
        """ returns the string representstion of Rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
