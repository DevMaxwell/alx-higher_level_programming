#!/usr/bin/python3
"""
function that adds 2 integers
"""


def add_integer(a, b=98):
    """ Return the addition of two numbers if they are a float or int type """
    if type(a) is int or type(a) is float:
        if type(b) is int or type(b) is float:
            return (int(a) + int(b))
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
