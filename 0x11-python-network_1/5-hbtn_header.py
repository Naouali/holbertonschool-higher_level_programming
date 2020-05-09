#!/usr/bin/python3
"""
fetch headeds
"""


import requests


if __name__ == "__main__":
    data = requests.get("https://intranet.hbtn.io/status")
    print(data.headers["X-Request-Id"])
