#!/usr/bin/python3
import dis

def magic_calculation(a, b):
    result = 0
    for i in range(1,3):
        a = i


dis.dis(magic_calculation)