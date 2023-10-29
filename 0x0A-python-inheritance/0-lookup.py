#!/usr/bin/python3
""" loockup method module """


def lookup(obj):
    """ Returns the list of available attributes and methods of an object
        args:
            obj: The object
        returns:
            A list object of attributes """
    return dir(obj)
