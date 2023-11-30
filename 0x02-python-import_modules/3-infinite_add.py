#!/usr/bin/python3
def add_arg(argv):
    l = len(argv) - 1
    if l == 0:
        print("{:d}".format(l))
        return
    else:
        a = 1
        add = 0
        while a <= l:
            add += int(argv[a])
            a += 1
            print("{:d}".format(add))
