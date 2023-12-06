#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        nbr = 0
        d = 0
        for t in my_list:
            nbr += (t[0] * t[1])
            d += t[1]
            return (nbr / d)
        return 0

