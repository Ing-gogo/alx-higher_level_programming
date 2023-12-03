#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_chr = sentence[0] if length > 0 else "None"
    tuplee = length, first_chr
    return (tuplee)
