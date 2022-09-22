#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    arg = sys.argv
    def calc(*param):
        nb = len(arg)
        res = "{} + {} = {}"
        if nb == 4:
            match arg[2]:
                case "+":
                    print(res.format(arg[1], arg[3], add(int(arg[1]),
                                                         int(arg[3]))))
                case "-":
                    print(res.format(arg[1], arg[3], sub(int(arg[1]),
                                                         int(arg[3]))))
                case "*":
                    print(res.format(arg[1], arg[3], mul(int(arg[1]),
                                                         int(arg[3]))))
                case "/":
                    print(res.format(arg[1], arg[3], div(int(arg[1]),
                                                         int(arg[3]))))
                case _:
                    print("Unknown operator. Available operators: +, -, * and /")
                    sys.exit(1)
            sys.exit(0)
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    calc(arg)
