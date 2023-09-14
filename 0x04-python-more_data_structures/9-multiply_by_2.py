#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    res = dict(a_dictionary)

    for key in res.keys():
        res[key] *= 2

    return res
