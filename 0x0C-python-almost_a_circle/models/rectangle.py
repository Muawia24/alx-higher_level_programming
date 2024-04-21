#!/usr/bin/python3
""" Rectangle class """
from models.base import Base


class Rectangle(Base):
    """
    Rectangle that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ class constructor """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ calculate area of rectangle """
        return self.__width * self.height

    def display(self):
        """
        prints in stdout the Rectangle instance
        with the character #
        """
        for r in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end='')
            print("#" * self.width)

    def __str__(self):
        """
         it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args):
        """
        assigns an argument to each attribute
        """
        arg = len(args)
        if arg >= 1:
            self.__id = args[0]
        if arg >= 2:
            self.__width = args[1]
        if arg >= 3:
            self.__height = args[2]
        if arg >= 4:
            self.__x = args[3]
        if arg == 5:
            self.__y = args[4]
