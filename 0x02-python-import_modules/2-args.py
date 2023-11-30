#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    ag = sys.argv
    size = len(ag) - 1

    if size > 1:
        print("{} arguments:".format(size))
        for a in range(1, size + 1):
            print("{}: {}".format(a, ag[a]))

    elif size == 0:
            print("{} arguments.".format(size))
    else:
            print("{} argument:".format(size))
            print("{}: {}".format(size, ag[1]))
