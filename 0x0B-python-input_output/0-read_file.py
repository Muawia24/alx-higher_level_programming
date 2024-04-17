#!/usr/bin/python3
""" read_file module """


def read_file(filename=""):
    """
     reads a text file (UTF8) and prints it to stdout
    """

    with open(filename, "r", encoding="utf-8") as f:
        for fd in f:
            print(fd, end='')
