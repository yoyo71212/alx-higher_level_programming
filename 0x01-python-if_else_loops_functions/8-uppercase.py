#!/usr/bin/python3
def uppercase(str):
    if len(str) <= 0:
        print("".format(), end="\n")
        return
    for i in range(len(str)):
        char = str[i]
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            char = chr(ord(str[i]) - 32)
        print("{}".format(char), end="\n" if i == len(str) - 1 else "")
