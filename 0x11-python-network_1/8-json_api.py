#!/usr/bin/python3
"""Write a Python script that takes in a letter
and sends a POST request to
http://0.0.0.0:5000/search_user with
the letter as a parameter"""
import requests
import sys


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}
    r = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        resp = r.json()
        if resp == {}:
            print("No result")
        else:
            print("[{}] {}".format(resp.get("id") resp.get("name")))
    except ValueError:
        print("Not a valid JSON")
