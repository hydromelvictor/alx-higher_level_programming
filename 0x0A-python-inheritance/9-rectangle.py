#!/usr/bin/python3
"""rectangle class inherit of BaseGeometry
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """BaseGeometry: superclass
    """
    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """area for rectangle
        """
        return self.__height * self.__width

    def __str__(self) -> str:
        """return renctangle description
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
