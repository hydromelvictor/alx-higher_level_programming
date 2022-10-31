#!/usr/bin/python3
"""create the rectanlge"""

from base import Base


class Rectanlge(Base):
    """class heritant de base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initiaidsation"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
