#!/usr/bin/python3
"""verify is class instance
"""


def is_kind_of_class(obj, a_class):
    """obj: object  verifying
        a_class: class
        return boolean
    """
    if isinstance(obj, a_class):
        return True

    return False
