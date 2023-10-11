#!/usr/bin/python3
"""defining read_file function"""


def read_file(filename=""):
    """Reads a file, filename, using utf-8 encoding"""

    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
