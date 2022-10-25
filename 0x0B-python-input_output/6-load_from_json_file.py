#!/usr/bin/python3
"""create object by json file
"""

import json


def load_from_json_file(filename):
    """filename: name of file
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
