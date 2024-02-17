import urllib.request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    page = response.read()
    print("- Body response:")
    print("\t- type: {}".format(type(page)))
    print("\t- content: {}".format(page))
