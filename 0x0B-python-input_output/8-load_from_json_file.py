#!/usr/bin/python3
"""
8
"""


import json


def load_from_json_file(filename):
    """
    load from json
    """
    with open(filename, 'r') as f:
        data = f.read()
        return (json.loads(data))
