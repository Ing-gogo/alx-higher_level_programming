#!/usr/bin/python3
def complex_delete(my_dict, value):
    keys_to_del = []
    for x in my_dict:
        if my_dict[x] == value:
            keys_to_del.append(x)
            for x in keys_to_del:
                del my_dict[x]
                return my_dict
