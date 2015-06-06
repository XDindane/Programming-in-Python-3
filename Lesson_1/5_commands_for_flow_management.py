#!/usr/bin/env python3
from random import randint

#--- command if
lines = randint(1, 11000)
print(lines)
if lines < 1000:
    print("small")
elif lines < 10000:
    print("medium")
else:
    print("big")

#--- command while
while True: # dont works becuase we didnt declare a functions
    break # break for skip exception
    item = some_function()
    if not item:
        break
    process_function()

#--- command for....in
countries = ["Denmark", "Finland","Norway", "Sweden"]
for country in countries:
    print(country)

for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    if letter in "AEIOU":
        print(letter, "is vowel")
    else:
        print(letter, "is consonant")

#--- exceptions
s = input("enter number: ")
try:
    i = int(s)
    print("entered a valid number:", i)
except ValueError as err: #throws when i= float and etc...
    print(err)

    
