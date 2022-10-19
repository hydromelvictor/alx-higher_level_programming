#!/usr/bin/python3

"""
    add_integer is a function for addition a and b
    a, b is integer or float number otherwise raise
"""

def add_integer(a, b=98):
    """return a + b if the conditions is ok"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    
    if type(a) is float:
        a = int(a)

    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(b) is float:
        b = int(b)

    return a + b
