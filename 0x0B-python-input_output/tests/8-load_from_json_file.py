#!/usr/bin/python3
"""
load fromjson file
"""


import json


def load_from_json_file(filename):
    with open(filename) as f:
        return json.load(f)
