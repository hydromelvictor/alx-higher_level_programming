#!/usr/bin/python

"""

"""


def matrix_mul(m_a, m_b):
    """
    
    """
    if type(m_a) is not list or type(m_b) is not list:
        raise TypeError("m_a must be a list or m_b must be a list")

    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")

        if i is None:
            raise ValueError("m_a can't be empty")

        size = len(m_a[0])
        
        for j in i:
            if j is None:
                raise ValueError("m_a can't be empty")

            if type(j) is not int and type(j) is not float:
                raise TypeError("m_a should contain only integers or floats")

        if len(i) != size:
            raise TypeError("each row of m_a must be of the same size")


    for j in m_b:
        if type(j) is not list:
            raise TypeError("m_b must be a list of lists")

        if j is None:
            raise ValueError("m_b can't be empty")

        size = len(m_b[0])
        
        for k in j:
            if k is None:
                raise ValueError("m_b can't be empty")

            if type(k) is not int and type(k) is not float:
                raise TypeError("m_b should contain only integers or floats")

        if len(j) != size:
            raise TypeError("each row of m_b must be of the same size")


    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m = []


print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))