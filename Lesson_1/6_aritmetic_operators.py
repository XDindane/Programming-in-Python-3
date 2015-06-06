#!/usr/bin/env python3

print(
    5+6,
    3-7,
    4*8)
print(12/3,3/2) # return float. typically for python, other lang. returns int.

a =5
a +=8
print(a) # fast entry

# strings
name = "John"
name += "Dudek"
print (name)

#lists
seeds = ["sezam", "sunflower"]
seeds += ["pumpkin"] # must be iterable
print(seeds)

#example of noniterable
#seeds += 5 #exceptions TypeError
seeds += [5] # OK
#string is iterable
seeds += "durian"  #iterrates over each letter, we can use append to add whole string
print(seeds) # prints ['sezam', 'sunflower', 'pumpkin', 5, 'd', 'u', 'r', 'i', 'a', 'n']


    
