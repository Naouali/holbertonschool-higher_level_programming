#!/usr/bin/python3
"""
module to post
data
"""


import requests
import sys


if __name__ == "__main__":
    payload = {"email": str(sys.argv[2])}
    data = requests.post(str(sys.argv[1]+"/post"), data=payload)
    print("You email is: {}".format(data.text["email"]))
