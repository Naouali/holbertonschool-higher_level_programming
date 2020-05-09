#!/usr/bin/python3
"""
module to fetch
api data
"""


import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    try:
        q = sys.argv[1]
    except:
        q = ""

    input_data = {'q': q}
    data = requests.post(url, input_data)
    try:
        print("[{}] {}".format(data.json()["id"], data.json()["name"]))
    except KeyError:
        print("No result")
    except ValueError:
        print("Not a valid JSON")
