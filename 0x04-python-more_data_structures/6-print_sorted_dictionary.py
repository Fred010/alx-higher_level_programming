#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    arranged_list = list(a_dictionary.keys())
    arranged_list.sort()
    for index in arranged_list:
        print("{}: {}".format(index, a_dictionary.get(index)))
