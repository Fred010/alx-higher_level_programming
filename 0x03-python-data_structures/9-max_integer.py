#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    bigint = my_list[0]
    for num in range(len(my_list)):
        if my_list[num] > bigint:
            bigint = my_list[num]

    return (bigint)
