#!/usr/bin/python3
"""
module to fetch
url
"""


import requests


data = requests.get("https://intranet.hbtn.io/status/")
print("Body response:")
print("\t - type: {}".format(type(data.text)))
print("\t - content: {}".format(data.text))
