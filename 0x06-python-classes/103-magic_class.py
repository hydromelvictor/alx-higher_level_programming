#!/usr/bin/python3
import dis
class MagicClass:
    """magic"""
    def __init__(self, raduis):
        self._MagicClass__radius = 0
        if type(raduis) is not int:
            raduis = 1
        if type(raduis) is not float:
            raduis = 2
            


dis.dis(MagicClass)