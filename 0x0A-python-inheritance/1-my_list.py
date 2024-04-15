#!/usr/bin/python3
""" MyList definition """


class MyList(list):
    """MyList class attributes"""
    def print_sorted(self):
        """Prints a sorted list"""

        print(sorted(self))
