#!/usr/bin/python3
"""my int version
"""


class MyInt(int):
    """int class inherit
    """

    def __eq__(self, other):
        """eq is ne
        """
        return int(self) != other

    def __ne__(self, other):
        """ne is eq
        """
        return int(self) == other
