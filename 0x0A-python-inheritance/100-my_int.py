#!/usr/bin/python3
""" MyInt module """


class MyInt(int):
    """ magic methods """

    def __eq__(self, other):
        """ returns inequality """
        return int(self) != int(other)

    def __ne__(self, other):
        """ returns equality """
        return int(self) == int(other)
