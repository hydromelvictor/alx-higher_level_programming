#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    str = []
    for i in matrix[:]:
        str.append(list(map(lambda j: j**2, i)))
    return str
