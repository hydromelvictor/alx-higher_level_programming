#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nb_arg = len(sys.argv)
    arg = ""
    if nb_arg == 2:
        arg = "argument:"
    else:
        if nb_arg == 1:
            arg = "arguments."
        else:
            arg = "arguments:"
    print("{} {}".format(nb_arg - 1, arg))
    for i in range(1, nb_arg):
        print("{}: {}".format(i, sys.argv[i]))
