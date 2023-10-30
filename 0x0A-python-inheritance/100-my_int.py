#!/usr/bin/python3
""" Module for MyInt class """


class MyInt(int):
    """ Defines MyInt class """
    def __new__(cls, *args, **kwargs):
        """ Creayes a new instance of MyInt """
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """ Inverts != to == """
        return int(self) != other

    def __ne__(self, other):
        """ Inverts == to != """
        return int(self) == other
