#!/usr/bin/env python3

import sys

#variables from source_codes
Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ",
        "   *  "]
Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

#TODO: bigDigits

try:
    numbers = sys.argv[1]
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(numbers):
            number = int(numbers[column]) # gets index for digits
            digit = Digits[number] # gets list of char from digits
            line += digit[row] +  " " # foreach line gets the right position of char
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: 8_making_and_calling_functions_bigdigits.py <number>")
except ValueError as err:
    print(err, "in", numbers)
    
