#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}
    if type(roman_string) != str:
        return 0
    ch = []
    for i in list(roman_string):
        ch.append(roman[i])
    for i in range(len(ch) - 1):
        if ch[i] < ch[i + 1]:
            ch[i] = -ch[i]
    return sum(ch)
