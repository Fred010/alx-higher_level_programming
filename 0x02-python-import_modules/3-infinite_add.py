#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    overall = 0
    for n in range(len(sys.argv) - 1):
        overall += int(sys.argv[n + 1])
    print("{}".format(overall))
