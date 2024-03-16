#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    if len(matrix) == 1:
        print()
        return
    for row in range(len(matrix)):
        for n in range(len(matrix)):
            if n == len(matrix) - 1:
                print("{:d}".format(matrix[row][n]), end='')
            else:
                print("{:d}".format(matrix[row][n]), end=" ")
        print()
