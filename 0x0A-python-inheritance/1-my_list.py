#!/usr/bin/python3
"""class inherit of list
"""


class MyList(list):
    """inehrit of list
    """

    def __init__(self):
        """initialisation for class
        """
        super().__init__()

    def print_sorted(self):
        """sort the list
        """
        print(sorted(self))
