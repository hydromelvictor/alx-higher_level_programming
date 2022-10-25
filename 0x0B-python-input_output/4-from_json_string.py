#!/usr/bin/python3
"""json serialize object
"""

from io import StringIO
import json

def from_json_string(my_str):
    """ my_str: data format serialize in json
    """
    io = StringIO()
    json.dump(my_str, io)
    return io.getvalue()
