#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    if not matrix:
        print()
        return
    for row in matrix:
        for n in row:
            if row.index(n) == len(row) - 1:
                print("{:d}".format(n), end='')
            else:
                print("{:d}".format(n), end=" ")
        print()
