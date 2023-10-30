#!/usr/bin/python3
""" Module for BaseGeometry class"""


class BaseGeometry:
    """ Defines BaseGeometry class """
    def area(self):
        """ Returns the area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates a value """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
