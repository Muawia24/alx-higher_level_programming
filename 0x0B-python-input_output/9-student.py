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

    def to_json(self):
        """
        retrieves a dictionary representation of a
        Student instance
        """
        d = {}
        for key, value in self.__dict__.items():
            if type(value) in [list, dict, str, bool, int]:
                d[key] = value

        return d
