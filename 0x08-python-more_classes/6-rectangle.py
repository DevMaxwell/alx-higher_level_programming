#!/usr/bin/python3
"""
class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    class Rectangle that define a rectangle
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        width -> rectangle width, height -> height of rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """  get width """
        return self.__width

    @width.setter
    def width(self, value):
        """ width property setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height property getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height property setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """ customize __str__ medthod """
        myStr = ""
        if self.__weight != 0 or self.__height != 0:
            for i in range(self.__height):
                for j in range(self.__weight):
                    myStr += "#"
                if i < self.height - 1:
                    myStr += "\n"
        return myStr

    def __repr__(self):
        """ customize custom __repr__ method """
        myRepr = ""
        myPepr += "Rectangle(' + str(self.__width) + ",
        myRepr += " + str(self.__height)+ ')"

    def __del__(self):
        """ return 'Bye Rectangle..' when an instance is deleted"""
        type(self).number_of_instances -= 1
        print('Bye rectangle...')
