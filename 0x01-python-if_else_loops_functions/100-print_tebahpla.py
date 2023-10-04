#!/usr/bin/python3
c = 0
for n_char in range(ord("z"), ord("a") - 1, -1):
    print("{}".format(chr(n_char - c)), end="")
    c = 32 if c == 0 else 0
