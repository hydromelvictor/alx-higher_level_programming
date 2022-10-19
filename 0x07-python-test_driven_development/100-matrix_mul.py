#!/usr/bin/python3

"""
    matrix function complete
"""


def matrix_mul(m_a, m_b):
    """
        m_a: array of integer or float
    """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")

    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")

    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")

        if len(i) == 0:
            raise ValueError("m_a can't be empty")

        size = len(m_a[0])

        if len(i) != size:
            raise TypeError("each row of m_a must be of the same size")
        
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_a should contain only integers or floats")


    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    for j in m_b:
        if type(j) is not list:
            raise TypeError("m_b must be a list of lists")

        if len(j) == 0:
            raise ValueError("m_b can't be empty")

        size = len(m_b[0])

        if len(j) != size:
            raise TypeError("each row of m_b must be of the same size")
        
        for k in j:
            if type(k) is not int and type(k) is not float:
                raise TypeError("m_b should contain only integers or floats")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    matrix = []
    for i in range(len(m_a)):
        line = []
        for j in range(len(m_b[0])):
            n = 0
            for k in range(len(m_a[0])):
                n += m_a[i][k] * m_b[k][j]
            line.append(n)
        matrix.append(line)

    return matrix