#!/usr/bin/python3
def weight_average(my_list=[]):
    res = 0
    num = 0
    den = 0

    for x in my_list:
        num += x[0] * x[1]
        den += x[1]

    if den != 0:
        res = num / den

    return res
