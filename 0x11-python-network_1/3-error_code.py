#!/usr/bin/python3
"""
scsript that takes and sends URL and displays response
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    page_req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(page_req) as response:
            page = response.read().decode("ascii")
            print(page)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
