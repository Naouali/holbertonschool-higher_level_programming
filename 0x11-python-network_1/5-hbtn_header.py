#!/usr/bin/python3
"""
fetch headeds
"""


import requests
import sys


if __name__ == "__main__":
    data = requests.get(str(sys.argv[1]))
    print(data.headers["X-Request-Id"])
