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
