#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        temp = i % 15
        if temp == 0:
            print("FizzBuzz", end=" ");
        elif temp == 3 or temp == 6 or temp == 9 or temp == 12:
            print("Fizz", end=" ")
        elif temp == 5 or temp == 10:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")

