#!/usr/bin/python3
"""rectangle class
"""

from base import Base



class Rectangle(Base):
    """class inheritance of Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ width: rectangle width
            height: rectangle height
            x: coord for i
            y: coord for j
        """
        super().__init__(id)

        if type(width) is not int:
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")

        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
