#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        str = list(my_string)
        for i in str:
            if i == 'c' or i == 'C':
                str.remove(i)
            my_string = ""
        for i in str:
            my_string += i
        return my_string
