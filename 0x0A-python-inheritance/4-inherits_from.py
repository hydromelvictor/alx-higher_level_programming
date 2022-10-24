#!/usr/bin/python3
"""verify is class instance
"""


def inherits_from(obj, a_class):
    """obj: object  verifying
        a_class: class
        return boolean
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True

    return False
