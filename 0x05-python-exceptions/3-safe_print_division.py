#!/usr/bin/python3
def safe_print_division(a, b):
    """function returning division of a by b"""
    try:
        q = a / b
    except (TypeError, ZeroDivisionError):
        q = None
    finally:
        print("Inside result: {}".format(q))
        return (q)


