#!/usr/bin/python3

"""
    square function programming
"""


def print_square(size):
    """
        size: square size
        print the square show in '#'
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise TypeError("size must be >= 0")

    for i in range(size):
        print("{}".format("#" * size))
