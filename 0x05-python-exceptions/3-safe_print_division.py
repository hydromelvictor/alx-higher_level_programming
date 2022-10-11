#:/usr/bin/python3
def safe_print_division(a, b):
    c = 0
    try:
        print("Inside result: {:.1f}".format(a / b))
    except ZeroDivisionError:
        print("Inside result: {}".format(None))
        return None
    finally:
        return c
