#!/usr/bin/python3
"""
add argument to json
"""

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file =__import__('8-load_from_json_file').load_from_json_file
import os
import sys

my_list = []
for i in sys.argv[1:]:
    my_list.append(i)
save_to_json_file(my_list,'add_item')
load_from_json_file('add_item')
