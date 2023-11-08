#!/usr/bin/python3
"""Define a class called student"""


class Student:
    """Representing an individual students."""

    def __init__(self, first_name, last_name, age):
        """intialize a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dict representation of class Student"""
        return self.__dict__
