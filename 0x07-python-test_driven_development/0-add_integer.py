#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Returns: Addition of two numbers

    """
    if not (isinstance(a, (int, float))) or not a:
        raise TypeError("a must be an integer")
    if not (isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    if not (isinstance(a, int)):
        a = int(a)
    if not (isinstance(b, int)):
        b = int(b)

    return a + b
