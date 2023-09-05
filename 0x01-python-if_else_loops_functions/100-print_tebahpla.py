#!/usr/bin/python3
upper = False
for i in range(122, 96, -1):
    char = ""
    if upper:
        char = chr(i - 32)
    else:
        char = chr(i)
    upper = not (upper)
    print("{}".format(char), end="")
