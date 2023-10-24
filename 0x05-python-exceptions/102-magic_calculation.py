#!/usr/bin/python3
def magic_calculation(a, b):
    outcome = 0
    for index in range(1, 13):
        try:
            if index > a:
                raise Exception("Too far")
            outcome += a ** b / index
        except Exception:
            outcome = b + a
            break
    return outcome
