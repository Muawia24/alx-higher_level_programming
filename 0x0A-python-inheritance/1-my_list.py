#!/usr/bin/python3
""" Mylist definition """


class MyList(list):
    """
    MyList class attributes
    """

    def print_sorted(self):
        """Prints a sorted list"""

        print(sorted(self))
