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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        method to save
        to files
        """
        f = cls.__name__ + ".json"
        m = []
        if list_objs is None:
            with open(f, mode="w") as fp:
                fp.write(cls, to_json_string(m))
        else:
            with open(f, mode="w") as fp:
                for item in list_objs:
                    m.append(item.to_dictionary())
                fp.write(cls.to_json_string(m))
