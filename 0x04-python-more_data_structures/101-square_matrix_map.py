#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    res = map(lambda row: [x ** 2 for x in row], matrix)
    return list(res)
