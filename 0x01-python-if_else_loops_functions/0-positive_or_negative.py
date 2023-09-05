#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    s = "is positive"
elif number == 0:
    s = "is zero"
else:
    s = "is negative"
print(" {:d} is {:s}.".format(number, s))
