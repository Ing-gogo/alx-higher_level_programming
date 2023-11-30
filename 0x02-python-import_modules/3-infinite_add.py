#!/usr/bin/python3
if __name__ == "__main__":
    import sys, math
    result = 0
    for a in sys.argv:
        result += int(a)
        print("{}".format(result))
