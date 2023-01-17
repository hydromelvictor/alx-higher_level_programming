#!/usr/bin/python3
"""Write a Python script that takes
in a URL and an email"""
import urllib.request
import urllib.parse
import sys


if __name__ = "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
