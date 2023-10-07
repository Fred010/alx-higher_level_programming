#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    sum_up = len(sys.argv) - 1
    if sum_up == 0:
        print("0 arguments.")
    elif sum_up == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(sum_up))
    for n in range(sum_up):
        print("{}: {}".format(n + 1, sys.argv[n + 1]))
