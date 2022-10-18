#!/usr/bin/python3
def magic_string(s = []):
    s.append("BestSchool")
    return ", ".join(s)


for i in range(10):
    print(magic_string())