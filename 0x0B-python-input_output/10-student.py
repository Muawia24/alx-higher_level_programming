#!/usr/bin/python3
""" Student module """


class Student:
    """
    that defines a student by,
    it first, last name and age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a
        Student instance
        """
        if attrs is not None:
            keys = [name for name in self.__dict__ if name in attrs]
        else:
            keys = [name for name in self.__dict__]

        d = {}
        for key in keys:
            value = getattr(self, key)
            if type(value) in [list, dict, str, bool, int]:
                d[key] = value

        return d
