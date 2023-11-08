#!/usr/bin/python3
"""Define a class student"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """initialize a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dict rep of a student"""
        object = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return object

            dict_list = {}

            for i in range(len(attrs)):
                for j in object:
                    if attrs[i] == j:
                        dict_list[j] = object[j]
            return dict_list
        return object
