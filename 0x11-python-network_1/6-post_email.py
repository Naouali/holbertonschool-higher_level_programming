#!/usr/bin/python3
"""
module to post
data
"""


import requests
import sys

payload = {"email": str(sys.argv[2])}
data = requests.post(str(sys.argv[1]+"/post"), data=payload)
print("you email is: {}".format(data.text["email"]))
