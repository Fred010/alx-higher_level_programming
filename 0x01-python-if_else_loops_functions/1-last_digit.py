#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)
modulus = number % 10 if number > 10 else number % -10
print("Last digit of {:d} is {:d} and is ".format(number, modulus), end="")
if modulus > 5:
    print("and is greater than 5")
elif modulus == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
