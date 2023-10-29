#!/usr/bin/python3
""" Defines a Rectangle """


class Rectangle:
    """ Rectangle class """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Initializes the Rectangle """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ width Getter """
        return self.__width

    @width.setter
    def width(self, width):
        """ width setter """
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')

        self.__width = width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, height):
        """ height setter """
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')

        self.__height = height

    def area(self):
        """ Returns the area of the Rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns the perimeter of the Rectangle """
        if (self.__width == 0 or self.__height == 0):
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """ Prints the Rectangle with the character '#' """
        if self.__width and self.__height:
            return (((str(self.print_symbol) * self.__width) + '\n')
                    * self.__height)[:-1]
        return ''

    def __repr__(self):
        """ Return a string representation of the Rectangle for recreation """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ Prins a message when an instance of Rectangle is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
