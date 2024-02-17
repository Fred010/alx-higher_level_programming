"""Fetches https://alx-intranet.hbtn.io/status using urllib."""

import urllib


def fetch_status():
    """
    Fetches the status from https://alx-intranet.hbtn.io/status using urllib.

    Prints the body of the response with tabulation before each line.
    """
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.urlopen(url) as response:
        body = response.read()
        print("\n".join(["\t- " + line for line in body.splitlines()]))


if __name__ == "__main__":
    fetch_status()
