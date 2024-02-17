import urllib

url = "https://alx-intranet.hbtn.io/status"

with urllib.urlopen(url) as response:
    body = response.read()
    print("- Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
