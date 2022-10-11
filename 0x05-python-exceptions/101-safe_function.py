#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    a = None
    try:
        a = fct(*args)
    except BaseException as err:
        sys.stderr.write("Exception: {}\n".format(err))
        a = None
    return a
