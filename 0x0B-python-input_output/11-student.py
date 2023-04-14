#!/usr/bin/python3
""" 11. Student to disk and reload """


class Student():
    """a class Student that defines a student by: (based on 10-student.py)"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        return {attr: self.__dict__[attr] for attr in attrs
                if attr in self.__dict__}

    def reload_from_json(self, json):
        for k in json:
            setattr(self, k, json[k])
