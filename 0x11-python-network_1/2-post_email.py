#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email
  - Displays the body of the response decoded in utf-8
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        page = response.read().decode("utf-8")
        print(page)