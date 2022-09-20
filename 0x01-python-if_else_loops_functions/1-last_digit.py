#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of {} is {} and is {}"
i = number % 10
if i > 5:
    print(str.format(number, i, "the string and is greater than 5"))
elif i == 0:
    print(str.format(number, i, i))
elif i < 6 and i != 0:
    print(str.format(number, i, "less than 6 and not 0"))
