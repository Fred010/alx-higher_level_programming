#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    request = requests.get("https://alx-intranet.hbtn.io/status")
    motif = request.text

    print("Body response:")
    print("\t- type: {}".format(type(motif)))
    print("\t- content: {}".format(motif))
