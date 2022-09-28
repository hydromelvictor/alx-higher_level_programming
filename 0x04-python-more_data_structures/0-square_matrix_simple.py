#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    str = []
    for i in matrix[:]:
        str.append([j**2 for j in i])
    return str
