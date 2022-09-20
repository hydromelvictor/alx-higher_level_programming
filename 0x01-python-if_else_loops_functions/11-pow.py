#!/usr/bin/python3
def pow(a, b):
    res = 1
    if b == 0:
        return 1
    else:
        if b < 0:
            a, b = 1/a, - b
        for i in range(b):
            res *=a
    return res
