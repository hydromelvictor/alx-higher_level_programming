#!/usr/bin/python3
"""square class inherit of rectangle
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Rectangle: class inherit of BaseGeometry
    """
    def __init__(self, size):
        """size: limit
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area for square
        """
        return self.__size ** 2

    def __str__(self):
        """square implement
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
