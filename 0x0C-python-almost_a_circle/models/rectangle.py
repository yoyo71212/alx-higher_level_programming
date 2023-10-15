#!/usr/bin/python3
""" Rectangle class module """


from models.base import Base


class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Get Width of Rectangle """
        return self.__width

    @width.setter
    def width(self, width):
        self.validate('width', width, False)
        self.__width = width

    @property
    def height(self):
        """ Get height of Rectangle """
        return self.__height

    @height.setter
    def height(self, height):
        self.validate('height', height, False)
        self.__height = height

    @property
    def x(self):
        """ Get x of Rectangle """
        return self.__x

    @x.setter
    def x(self, x):
        self.validate('x', x)
        self.__x = x

    @property
    def y(self):
        """ Get y of Rectangle """
        return self.__y

    @y.setter
    def y(self, y):
        self.validate('y', y)
        self.__y = y

    def validate(self, prop, val, eq=True):
        """ Validation method """
        if type(val) != int:
            raise TypeError('{} must be an integer'.format(prop))
        if eq and val < 0:
            raise ValueError('{} must be >= 0'.format(prop))
        if not eq and val <= 0:
            raise ValueError('{} must be > 0'.format(prop))

    def area(self):
        """ Method to get the area of the Rectangle """
        return self.width * self.height

    def display(self):
        """ Method to display the Rectangle """
        res = '\n' * self.y + \
                ((' ' * self.x) + ('#' * self.width) + '\n') * self.height
        print(res, end='')

    def __str__(self):
        return ('[{}] ({}) {}/{} - {}/{}'). \
                format(type(self).__name__, self.id, self.x, self.y, self.width, self.height)
