#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):

    new_d = dict(sorted(a_dictionary.items()))
    for k, v in new_d.items():
        print("{}: {}".format(k, v))
