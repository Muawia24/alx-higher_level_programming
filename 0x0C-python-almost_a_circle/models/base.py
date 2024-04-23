#!/usr/bin/python3
""" Base class """
import json
import os


class Base:
    """ Base methods """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        that returns the JSON string representation
        of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        (cls, list_objs): that writes the JSON string
        representation of list_objs to a file
        """
        fname = cls.__name__ + ".json"
        if list_objs is None:
            with open(fname, "w") as fil:
                fil.write("[]")
        else:
            with open(fname, "w") as f:
                f.write(cls.to_json_string(list(map(
                                                lambda x: x.to_dictionary(),
                                                list_objs))))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dum = cls(3, 3)
        if cls.__name__ == "Square":
            dum = cls(3)
        dum.update(**dictionary)
        return dum

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        fname = cls.__name__ + ".json"
        if not os.path.exists(fname):
            return []
        with open(fname, "r") as f:
            return [cls.create(**x) for x in
                    cls.from_json_string(f.read())]
