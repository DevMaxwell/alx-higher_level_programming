#!/usr/bin/python3
""" returns the list of available attributes and methods of an object """


def lookup(obj):
    """ return a list of objects and methods available """
    return (dir(obj))
