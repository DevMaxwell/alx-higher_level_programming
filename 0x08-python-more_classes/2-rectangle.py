#!/usr/bin/python3
"""
class Rectangle that defines a rectangle
"""


class Rectangle:
"""
class Rectangle that defines a rectangle
"""

    def __init__(self, width = 0, height = 0):
        """
        width -> rectangle width, height -> height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """  get width """
        return self.__width

    @width.setter
    def width(self, value):
        """ width property setter """
        if value.isdigit():
            self.__width = value
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer") 

    @property
    def height(self):
        """ height property getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height property setter """
        if value.isdigit():
            self.__height = value
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """ area of rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height *2))
