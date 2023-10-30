#!/usr/bin/python3
""" Module for Rectangle class """


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Defines Rectangle class """
    def __init__(self, width, height):
        """ Rectangle constructor """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Returns the area of the Rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Returns the string representation of the Rectangle """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
