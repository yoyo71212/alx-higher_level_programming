#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    c = len(sys.argv) - 1
    if c != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>"); exit(1)

    res = 0
    if sys.argv[2] == "+":
        res = add(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == "-":
        res = sub(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == "*":
        res = mul(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == "/":
        res = div(int(sys.argv[1]), int(sys.argv[3]))
    else:
        print("Unknown operator. Available operators: +, -, * and /"); exit(1)

    print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], res))
