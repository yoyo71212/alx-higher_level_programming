#!/usr/bin/python3
""" Module for Square class """


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Defines Square class """
    def __init__(self, size):
        """ Square constructor """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Returns the area of a Square """
        return self.__size ** 2
