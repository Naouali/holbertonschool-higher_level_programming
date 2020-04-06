#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as f:
        data = f.write(str(my_obj))
        new = json.dumps(data)
        return new
        
