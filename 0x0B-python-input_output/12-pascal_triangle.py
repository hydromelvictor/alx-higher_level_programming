#!/usr/bin/python3
""" technical interview
"""


def factors(n):
    """factorial
    """
    res = 1
    for i in range(1, n + 1):
        res *= i

    return res


def combine(p, n):
    """combinaison
    """
    return factors(n) // (factors(p) * factors(n-p))


def pascal_triangle(n):
    """pascal triangle for n
    """
    if n <= 0:
        return []

    pas = []
    for i in range(n):
        pascal = []
        for j in range(i+1):
            pascal.append(combine(j, i))
        pas.append(pascal)

    return pas
