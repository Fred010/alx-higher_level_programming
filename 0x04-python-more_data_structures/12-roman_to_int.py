#!/usr/bin/python3


def to_subtract(list_num):
    sub_num = 0
    max_num = max(list_num)

    for n in list_num:
        if max_num > n:
            sub_num += n

    return (max_num - sub_num)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_num =\
            {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_n.keys())

    num = 0
    last_rom = 0
    list_num = [0]

    for c in roman_string:
        for r_num in list_keys:
            if r_num == c:
                if roman_num.get(c) <= last_rom:
                    num += to_subtract(list_num)
                    list_num = [roman_num.get(c)]
                else:
                    list_num.append(roman_num.get(c))

                last_rom = roman_num.get(c)

    num += to_subtract(list_num)

    return (num)
