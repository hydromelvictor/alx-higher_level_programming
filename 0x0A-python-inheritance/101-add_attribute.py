#!/usr/bin/python3
"""add the new attribute
"""


def add_attribute(obj, attr, value):
    """ obj: object
        attr: attribute
        value: attribute value
    """
    if attr in obj.__dict__ or attr in obj.__dir__:
        raise TypeError("can't add new attribute")

    obj.attr = value
