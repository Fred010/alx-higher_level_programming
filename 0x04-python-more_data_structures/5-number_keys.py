#!/usr/bin/python3


def number_keys(a_dictionary):
    num_of_keys = 0
    key_count = list(a_dictionary.keys())

    for i in key_count:
        num_of_keys += 1

    return (num_of_keys)
