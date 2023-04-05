#!/usr/bin/python3
"""
class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    class Rectangle that define a rectangle
    """

    def __init__(self, width=0, height=0):
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

    def area(self):
        """return area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.width * 2) + (self.__height * 2)
