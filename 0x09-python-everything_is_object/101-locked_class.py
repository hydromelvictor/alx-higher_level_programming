#!/usr/bin/python3

class LockedClass:
    """
        lockedclass
        __init__ function
    """
    def __init__(self):
        self.__slots__ = ('first_name', )
