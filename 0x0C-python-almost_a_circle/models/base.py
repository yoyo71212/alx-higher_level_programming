#!/usr/bin/python3
""" Base class """


from json import dumps, loads


class Base:
    """ Base of OOP hierarchy"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries:
            return dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w",
                  encoding="utf-8") as file:
            file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string """
        if json_string:
            return loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        from models.square import Square
        from models.rectangle import Rectangle

        if cls is Rectangle:
            res = Rectangle(1, 1)
        elif cls is Square:
            res = Square(1)
        else:
            res = None

        res.update(**dictionary)
        return res
