#!/usr/bin/python3
"locked class"


class LockedClass:
    """
    only allow instance with attributes 'first_name
    """


    __slots__ = ["first_name"]
