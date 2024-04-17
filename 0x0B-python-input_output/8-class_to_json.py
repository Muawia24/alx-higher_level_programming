#!/usr/bin/python3
""" class to json module """


def class_to_json(obj):
    """
     returns the dictionary description with simple data
     structure (list, dictionary,
     string, integer and boolean) for JSON
    """
    d = {}
    for key, value in obj.__dict__.items():
        if type(value) in [list, dict, str, bool, int]:
            d[key] = value

    return d
