#!/usr/bin/python3
""" Square class module """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns a string of the Square's information """
        return ('[{}] ({}) {}/{} - {}'). \
            format(type(self).__name__, self.id,
                   self.x, self.y, self.width)

    @property
    def size(self):
        """ Get size of Square """
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __update(self, id=None, size=None, x=None, y=None):
        """ Method that handles updating the Square """
        if id:
            self.id = id
        if size:
            self.size = size
        if x:
            self.x = x
        if y:
            self.y = y

    def update(self, *args, **kwargs):
        """ Method to update the Square """
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)
