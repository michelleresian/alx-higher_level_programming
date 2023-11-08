#!/usr/bin/python3
"""module for the funtion that return a dict description"""


def class_to_json(obj):
    """function to return the dict with simple data structures."""
    return obj.__dict__
