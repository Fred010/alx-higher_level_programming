#!/usr/bin/python3


def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    index = 0

    for n in uniq_list:
        index += n

    return (index)
