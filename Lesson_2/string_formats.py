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

#--- to be continued
