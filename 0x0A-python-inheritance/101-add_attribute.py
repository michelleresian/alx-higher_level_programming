#!/usr/bin/python3
"""atribute function docs"""


def add_attribute(object, attribute, att_value):
    """function to set an attribute"""
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, attribute, att_value)
