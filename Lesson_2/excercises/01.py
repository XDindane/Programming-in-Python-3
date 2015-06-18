#!/usr/bin/env python3

import sys
import unicodedata


def print_unicode_table(words):
    print(words)
    print("desítk.  hexa.  znak  {0:^40}".format("název"))
    print("-------  -----  ----  {0:-<40}".format(""))

    code = ord(" ")
    end = min(0xD800, sys.maxunicode)

    while code < end:
        c = chr(code)
        name = unicodedata.name(c, "*** neznámé ***")
        ok = True # true or if one element in list does not match - set False and dont print
        for word in words:
            if word is None or word not in name.lower(): #if not match skip and dont print
                ok = False
                break
        if ok: # if we found a match of all parameters print it.
            print("{0:7}  {0:5X}  {0:^3c}  {1}".format(code, name.title()))
        code += 1


words = []
if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("použití: {0} [řetězec1 [řetězec2 [... řetězecN]]]".format(sys.argv[0]))
        words = None
    else:
        for arg in sys.argv: 
            if sys.argv[0] != arg: # or can use a sys,argv[1:]
                words.append(arg.lower())
        
if words != 0:
    print_unicode_table(words)
