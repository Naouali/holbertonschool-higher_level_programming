#!/usr/bin/python3
"""
module to reture dict from class
"""


def class_to_json(obj):
    """
    function to return dictionary
    representation f obj
    """

    return (obj.__dict__)
