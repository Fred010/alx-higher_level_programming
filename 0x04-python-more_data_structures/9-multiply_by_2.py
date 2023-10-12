#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    list_keys = list(new_dict.keys())

    for index in list_keys:
        new_dict[index] *= 2

    return (new_dict)
