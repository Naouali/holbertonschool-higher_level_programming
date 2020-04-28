#!/usr/bin/python3
"""
 Class Base:
        private class attribute __nb_objects = 0
        class constructor: def __init__(self, id=None)::
"""


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        return json representation
        """
        import json
        if len(list_dictionaries) == 0 or list_dictionaries is None:
            return "[]"
        return (json.dumps(list_dictionaries))
