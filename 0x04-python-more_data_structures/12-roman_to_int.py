#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    d = [roman_dict[a] for a in roman_string]
    output = 0
    for x in range(len(d)):
        output += d[x]
        if d[x - 1] < d[x] and x != 0:
            output -= (d[x - 1] + d[x - 1])
            return output



