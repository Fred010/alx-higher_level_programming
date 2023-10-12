#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    key_pair_list = list(a_dictionary.keys())

    for dict_val in key_pair_list:
        if value == a_dictionary.get(dict_val):
            del a_dictionary[dict_val]

    return (a_dictionary)
