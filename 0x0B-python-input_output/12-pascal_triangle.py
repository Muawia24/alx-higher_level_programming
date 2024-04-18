#!/usr/bin/python3
""" pascal triangle module """


def pascal_triangle(n):
    """
     returns a list of lists of integers representing
     the Pascal’s triangle of n
    """

    triangle = []
    x = []
    y = []

    while n > 0:
        x = y
        y = y + [1]

        i = 1
        while i < len(x):
            y[i] = x[i - 1] + x[i]
            i += 1
        triangle.append(y)
        n -= 1

    return triangle
