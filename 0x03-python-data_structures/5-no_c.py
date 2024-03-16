#!/usr/bin/env python3
def no_c(my_string):

    """
    Removes all characters c and C from a string
    ...

    Parameters
    ----------
    my_string : str
        The string to remove 'Cc' from

    Return:
        The new string
    """
    if my_string:
        new_str = ""
        for char in my_string:
            if char not in "Cc":
                new_str += char
        return new_str
