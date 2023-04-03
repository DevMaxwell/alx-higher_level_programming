#!/usr/bin/python3
"""
class Rectangle that defines a rectangle
"""


class Rectangle:

    def __init__(self, width = 0, height = 0):
        """
        width -> rectangle width, height -> height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer") 

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
