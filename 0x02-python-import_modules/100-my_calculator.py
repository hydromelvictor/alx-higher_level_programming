#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    nb = len(argv)
    res = "{:d} + {:d} = {:d}"
    if nb == 4:
        match argv[2]:
            case "+":
                print(res.format(argv[1], argv[3], add(int(argv[1]),
                                                       int(argv[3]))))
            case "-":
                print(res.format(argv[1], argv[3], sub(int(argv[1]),
                                                       int(argv[3]))))
            case "*":
                print(res.format(argv[1], argv[3], mul(int(argv[1]),
                                                       int(argv[3]))))
            case "/":
                print(res.format(argv[1], argv[3], div(int(argv[1]),
                                                       int(argv[3]))))
            case _:
                print("Unknown operator. Available operators: +, -,\
                    * and /")
                quit(1)
        quit(0)
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    quit(1)
