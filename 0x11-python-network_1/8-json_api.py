#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    quest = sys.argv[1] if len(sys.argv) > 1 else ""

    motif = {'quest': quest}
    response = requests.post(url, data=motif)

    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data.get("id"), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
