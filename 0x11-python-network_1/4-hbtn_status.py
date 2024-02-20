#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    response = requests.get(url)
    motif = response.txt

    print("Body response:")
    print("\t- type: {}".format(type(motif)))
    print("\t- content: {}".format(motif))
