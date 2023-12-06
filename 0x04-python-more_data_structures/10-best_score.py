#!/usr/bin/python3
def best_score(my_dict):
    if my_dict and len(my_dict):
        great = list(my_dict.keys())[0]
        for x in my_dict:
            if my_dict[x] > my_dict[great]:
                great = key
                return great
            return None
