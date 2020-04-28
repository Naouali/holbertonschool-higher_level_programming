#!/usr/bin/python3
"""
 Class Base:
        private class attribute __nb_objects = 0
        class constructor: def __init__(self, id=None)::
"""
import json


class Base:
    """
    base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        return json representation
        """
        if len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
