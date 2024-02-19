#!/usr/bin/python3
"""displays the header variable of a request to a given URL"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    page_req = urllib.request.Request(url)
    with urllib.request.urlopen(page_req) as response:
        print(dict(response.headers).get("X-Request-Id"))
