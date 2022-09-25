#!/usr/bin/python3
def no_c(my_string):
    str = ""
    for i in my_string:
        if i != 'c' or i != 'C':
            str += i
    return str
