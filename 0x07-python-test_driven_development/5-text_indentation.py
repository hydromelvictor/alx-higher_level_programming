#!/usr/bin/python

"""
    function print the arguments text with 
    back new ligne if character is '.' or ':' or '?' 
"""


def text_indentation(text):
    """
        text: text aguments
        print text
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    s = ""

    for i in text:
        if i == "." or i == "?" or i == ":":
            s += i
            print("{}".format(s.strip()))
            print(end="\n")
            s = ""
        else:
            s += i
    print("{}".format(s.strip()), end="")
