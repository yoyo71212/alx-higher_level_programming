#!/usr/bin/python3
""" Base class """


from json import dumps, loads
import csv


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

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        from os import path

        f = "{}.json".format(cls.__name__)
        if path.isfile(f):
            with open(f, "r", encoding="utf-8") as file:
                return [cls.create(**d)
                        for d in cls.from_json_string(file.read())]
        else:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Saves the object to a csv (Serializes ) """
        from models.square import Square
        from models.rectangle import Rectangle

        if list_objs:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y] for o in list_objs]

            with open('{}.csv'.format(cls.__name__), "w",
                      newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """ Loads the object from a csv (deserializes) """
        from models.square import Square
        from models.rectangle import Rectangle

        res = []
        with open('{}.csv'.format(cls.__name__), "r",
                  newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    temp = {"id": row[0], "width": row[1],
                            "height": row[2], "x": row[3], "y": row[4]}
                else:
                    temp = {"id": row[0], "size": row[1],
                            "x": row[2], "y": row[3]}

                res.append(cls.create(**temp))

        return res
