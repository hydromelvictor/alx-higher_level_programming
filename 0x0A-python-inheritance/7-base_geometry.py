#!/usr/bin/python3
"""empty class name basegeometry
"""


class BaseGeometry:
    """base geomety class
    """
    def area(self):
        """area define raise exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ name:
            value:
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
