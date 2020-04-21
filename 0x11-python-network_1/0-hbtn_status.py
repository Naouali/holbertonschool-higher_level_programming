#!/usr/bin/python3
"""
fetching data from the web
"""
from urllib import request


with request.urlopen("https://intranet.hbtn.io/status") as req:
    data = req.read()
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
    print("\t- utf8 content : {}".format(data.decode("utf-8")))
