#!/usr/bin/python3
def matrix_divided(matrix, div):
    new = []
    s = "matrix must be a matrix (list of lists) of integers/floats"
    m = "Each row of the matrix must have the same size"
    if not matrix:
        raise TypeError(s)
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, (int, float)) or not div:
        raise TypeError("div must be a number")

    for row in matrix:
        if not isinstance(row, list) or not row:
            raise TypeError(s)

        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError(s)

        for r in matrix:
            if len(r) != len(row):
                raise TypeError(m)

        new.append([round(element / div, 2) for element in row])

    return new
