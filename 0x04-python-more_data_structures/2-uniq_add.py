#!/usr/bin/python3
def uniq_add(my_list=[]):
    hashset = set()

    for x in my_list:
        hashset.add(x)

    res = 0
    for x in hashset:
        res += x

    return res
