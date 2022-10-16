#!/usr/bin/python

"""
    matrix_divided function programming
    division the the element the mattrix and return the new
    matrix
"""


def matrix_divided(matrix, div):

    """
        matrix: list of list and the element is integer or float
        div: divisor, type integer or float
        return : new matrix
    """

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")

    size = 0
    if type(matrix[0]) is list:
        size = len(matrix[0])
    else:
        raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")

    for row in matrix:

        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")

        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")

        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return list(map(lambda row:
                list(map(lambda x: round(x/div, 2), row)), matrix))
