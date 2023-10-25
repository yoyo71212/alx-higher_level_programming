#!/usr/bin/python3
""" Defines a Rectangle """


class Rectangle:
    """ Rectangle class """
    def __init__(self, width=0, height=0):
        """ Initializes the Rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width Getter """
        return self.__width

    @width.setter
    def width(self, width):
        """ width setter """
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')

        self.__width = width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, height):
        """ height setter """
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')

        self.__height = height
