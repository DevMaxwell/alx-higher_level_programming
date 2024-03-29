#!/usr/bin/python3
"""
function that prints a square with the character #
"""


def print_square(size):
    """ print # in size * size """
    if type(size) is not int or size is None:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
