#!/usr/bin/python3
"""Write a Python script that
takes your GitHub credentials"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    value = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=value)
    print(r.json.get("id"))
