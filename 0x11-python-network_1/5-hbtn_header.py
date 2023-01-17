#!/usr/bin/python3
"""Write a Python script that takes in a URL"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
