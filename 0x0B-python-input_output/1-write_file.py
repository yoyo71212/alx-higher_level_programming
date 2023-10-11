#!/usr/bin/python3
"""defining write_file function"""


def write_file(filename="", text=""):
    """Writes a file, filename, using utf-8 encoding"""

    with open(filename, "w", encoding='utf-8') as file:
        return file.write(text)
