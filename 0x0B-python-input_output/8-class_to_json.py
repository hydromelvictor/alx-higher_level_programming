#!/usr/bin/python3
"""print dictionnary of object
"""


def class_to_json(obj):
    """ obj: object
    """
    return obj.__dict__
