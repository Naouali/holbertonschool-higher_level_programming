#!/usr/bin/python3
"""
module to post
data
"""


import requests
import sys


if __name__ == "__main__":
    try:
        payload = {"email": str(sys.argv[2])}
        data = requests.post(str(sys.argv[1]), data=payload)
        print(data.text)
    except:
        pass
