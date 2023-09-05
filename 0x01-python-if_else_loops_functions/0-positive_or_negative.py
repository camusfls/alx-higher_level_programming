#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number >= 0:
    s = "positive"
else:
    s = "negative"
print(" {} is {}.".format(number, s))
