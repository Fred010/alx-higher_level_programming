#!/usr/bin/python3
for n_letter in range(97, 123):
    if chr(n_letter) is not "q" and chr(n_letter) is not "e":
        print("{}".format(chr(n_letter)), end="")
