#!/usr/bin/env python3

import sys
import random

def get_int(msg, minimum, default):
    while True:
        try:
            line = input(msg)
            if not line and default is not None: # if default is set
                return default
            i = int(line)
            if i < minimum: # if minimum is bigger then input value
                print("must be >=", minimum)
            else:
                return i
        except ValueError as err:
            print(err)


rows = get_int("rows: ", 1, None) # minimum 1 default none, required
columns = get_int("columns ", 1, None)  # minimum 1 default none, required
minimum = get_int("minimum (or Enter for 0): ", -10000000, 0)  # minimum -10000000, default 0

default = 1000 
if default < minimum: # if default is less than then minimum multiple twice
    default = 2 * minimum
maximum = get_int("maximum (or Enter for " + str(default) + "): ", minimum, default)


row = 0
while row < rows: # foreach rows
    line = ""
    column = 0
    while column < columns: #foreach columns
        i = random.randint(minimum, maximum)
        s = str(i)
        while len(s) < 10: # foreach row over then 10 items, only for better formatting
            s = " " + s
        line += s
        column += 1
    print(line)
    row += 1
