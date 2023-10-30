#!/usr/bin/python3
""" Module for Rectangle class """


BaseGeometry = __import__("7-base_geometry").BaseGeometry
class Rectangle:
    """ Defines Rectangle class """
    def __init__(self, width, height):
        """ Rectangle constructor """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
