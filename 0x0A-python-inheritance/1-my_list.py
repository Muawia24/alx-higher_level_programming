#!/usr/bin/python3
""" Mylist definition """


class MyList(list):
    """
    print_sorted method
    prints the list, but sorted
    """

    def print_sorted(self):
        print(sorted(self))
