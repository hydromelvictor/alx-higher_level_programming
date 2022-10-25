#!/usr/bin/python3
""" serialize function
"""

import json


def to_json_string(my_obj):
    """my_obj: object
    """
    return json.dumps(my_obj)
