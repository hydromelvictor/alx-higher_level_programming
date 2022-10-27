#!/usr/bin/python3
"""class base
"""


class Base:
    """base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """id: id for init
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
