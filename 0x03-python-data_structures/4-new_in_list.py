#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    new = []
    for i in my_list:
        new.append(i)
    if idx < 0 or idx > len(my_list) - 1:
        return new
    new[idx] = element
    return new
