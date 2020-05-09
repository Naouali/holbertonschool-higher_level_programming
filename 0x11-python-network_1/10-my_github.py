#!/usr/bin/python3
"""
fetch data from
github api
"""
import requests
import sys


if __name__ == "__main__":
    try:
        data = requests.get(
                'https://api.github.com/user',
                auth=requests.auth.HTTPBasicAuth(
                    sys.argv[1],
                    sys.argv[2]
                    )
                )
        print(data.json()['id'])
    except:
        print("None")
