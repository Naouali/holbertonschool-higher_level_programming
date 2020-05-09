#!/usr/bin/python3
"""
module to post
data
"""


import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post = {"email": email}
    data = urllib.parse.urlencode(post)
    data = data.encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as r:
        d = r.read()
        print(d.decode("utf-8"))
