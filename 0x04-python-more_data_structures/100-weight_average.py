#!/usr/bin/python3


def weight_average(my_list=[]):
    if not my_list:
        return 0

    numerator = 0
    denomintor = 0

    for assembly in my_list:
        numerator += assembly[0] * assembly[1]
        denomintor += assembly[1]

    return (numerator / denomintor)
