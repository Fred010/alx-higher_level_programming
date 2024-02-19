#!/usr/bin/python3
import urllib.request

"""
Checks if the script is being run directly (not imported as a module)
scripts to fetch the content of a URL
"""

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        page = response.read()
        utf8_content = page.decode('utf-8')

        print("Body response:")
        print("\t- type: {}".format(type(page)))
        print("\t- content: {}".format(page))
        print("\t- utf8 content: {}".format(utf8_content))
