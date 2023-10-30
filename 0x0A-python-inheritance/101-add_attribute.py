#!/usr/bin/python3
""" Module for add_attribute method """


def add_attribute(obj, att, val):
    """ Adds an attribute to an object if possible

        args:
            obj: The object
            att: The attribute
            val: The value

        raises:
            TypeError: If the object can’t have new attribute """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, val)
