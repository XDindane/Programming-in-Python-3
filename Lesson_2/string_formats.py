#!/usr/bin/env python3

# ----------------------- format

s = "Román '{0}' vyšel v roce {1}".format("těžké časy", 1854)
print(s)
s = "{{{0}}} {1} :-}}".format("i am in brackets", "and i not")
print(s)
s= "{0} {1} Kč".format("Debt is ", 200)
print(s)

x = "three"
s = "{0} {1} {2}"
s = s.format("My", x, "dots")
print(s)

# ----------------------- collections
print("{who} is {age} old".format(who="Jane", age="88"))

print("{who} was {0} last week".format(12,who="Jane")) # position arguments are always first.

stock = ["paper","notes","pens","pencils"]
print("We have {0[1]} and {0[2]} in warehouse".format(stock)) # formatting with list indexes

import math, sys
print("math.pi=={0.pi} sys.maxunicode=={1.maxunicode}".format(math,sys)) # imported packages as argument

element = "Silver"
number = 47
print("Element {number} is {element}".format(**locals())) # local variables, two stars for unwrapping


# ----------------------- converting
from decimal import *
import decimal

decimal.Decimal("3.4084")
Decimal('3.4084')
print(decimal.Decimal("3.4084"))

print("{0} {0!s} {0!r} {0!a}".format(decimal.Decimal("93.4")))


# ----------------------- specific formatting

s = "Blazing sword"
print ("{0}".format(s)) #default
print ("{0:25}".format(s)) #minimal width 25
print ("{0:>25}".format(s)) #align right, minimal width 25
print ("{0:^25}".format(s)) # align middle, minimal width 25
print ("{0:-^25}".format(s)) #adds -, align middl, minimal width 25
print ("{0:.<25}".format(s)) # add ., align left, minimal width 25
print ("{0:.10}".format(s)) #maximal width 10


maxwidth = 12
print("{0}".format(s[:maxwidth]))
print("{0}:.{1}".format(s, maxwidth))


print("{0:0=12}".format(8749203)) # adds null, minimal width 12
print("{0:0=12}".format(-8749203)) # adds null, minimal width 12
print("{0:012}".format(8749203)) # adds null to minimal width 12
print("{0:012}".format(-8749203)) # adds null to minimal width 12

print("{0:b} {0:o} {0:x} {0:X}".format(14613198)) # withou base sign (binary, oct, hex, hex uppercase)
print("{0:#b} {0:#o} {0:#x} {0:#X}".format(14613198)) # with base sign (binary, oct, hex, hex uppercase)


print("{0:,} {0:*>13,}".format(int(2.39432185e6))) # add stars before number

import locale
# set locale should be set before multithreding, beacause for each multiThr. is not safety
x,y = (1234567890, 1234.56)
locale.setlocale(locale.LC_ALL, "C")
print("{0:n} {1:n}".format(x,y)) # c == '1234567890 123.56
locale.setlocale(locale.LC_ALL, "")
print("{0:n} {1:n}".format(x,y)) # cz == '1 234 567 890 1 234,56

# same examples with real and imaginary numbers





