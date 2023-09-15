#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0

    for c in reversed(roman_string):
        if romans[c] * 5 > res:
            res += romans[c]
        else:
            res -= romans[c]

    return res
