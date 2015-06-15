#!/usr/bin/env python3

import sys
import unicodedata


def print_unicode_table(word):
    print("desítk.  hexa.  znak  {0:^40}".format("název"))
    print("-------  -----  ----  {0:-<40}".format(""))

    code = ord(" ")
    end = min(0xD800, sys.maxunicode)

    while code < end:
        c = chr(code)
        name = unicodedata.name(c, "*** neznámé ***")
        if word is None or word in name.lower():
            print("{0:7}  {0:5X}  {0:^3c}  {1}".format(
                  code, name.title()))
        code += 1


word = None
if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("použití: {0} [řetězec]".format(sys.argv[0]))
        word = 0
    else:
        word = sys.argv[1].lower()
if word != 0:
    print_unicode_table(word)
