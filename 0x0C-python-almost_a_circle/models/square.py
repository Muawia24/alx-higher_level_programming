#!/usr/bin/python3
""" square.py """
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Square constructor """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        returns string representation of Square
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        if args:
            arg = len(args)
            if arg >= 1:
                self.id = args[0]
            if arg >= 2:
                self.size = args[1]
            if arg >= 3:
                self.x = args[2]
            if arg == 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        returns the dictionary representation of a Square
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
