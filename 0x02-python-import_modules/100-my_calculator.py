#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit(1)
    else:
        func = [[add, "+"], [sub, "-"], [mul, "*"], [div, "/"]]
        for i in func:
            if argv[2] == i[1]:
                print("{} {} {} = {:d}".format(argv[1], i[1], argv[3],
                                               i[0](int(argv[1]),
                                                    int(argv[3]))))
                quit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            quit(1)
