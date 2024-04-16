#!/usr/bin/python3
""" Add attribute module """


def add_attribute(obj, attr_name, attr_value):
    """ sets new attribute """
    if hasattr(obj, "__dict__") or \
            (hasattr(obj, "__setattr__") and hasattr(obj, attr_name)):
        setattr(obj, attr_name, attr_value)

    else:
        raise TypeError("can't add new attribute")
