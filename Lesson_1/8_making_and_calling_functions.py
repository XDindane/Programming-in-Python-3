#!/usr/bin/env python3

import sys
import random

def get_int(msg):
    while True:
        try:
            i = input(msg)
            return i
        except ValueError as err:
            print(err)

age = get_int("how old are you?: ")
print (age)

print(sys.argv)

print(random.randint(1,10))
print(random.choice(["apple","banana", "pear", "plum"]))
