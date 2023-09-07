#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    c = len(sys.argv) - 1
    res = 0

    for i in range(c):
        res += int(sys.argv[i + 1])

    print(res)
