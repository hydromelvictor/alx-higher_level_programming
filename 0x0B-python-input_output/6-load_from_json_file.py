#!/usr/bin/python3
"""create object by json file
"""

import json


def load_from_json_file(filename):
    """filename: name of file
    """
    return json.load(filename)
