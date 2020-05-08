#!/usr/bin/python3
"""
module to fetch
data from the header
"""


from urllib import request
import sys

if __name__ == "__main__":
    with request.urlopen(str(sys.argv[1])) as data:
        header = data.getheaders()
        for x in header:
            if x[0] == "X-Request-Id":
                print(x[1])
