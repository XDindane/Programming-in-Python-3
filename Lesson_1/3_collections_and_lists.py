#!/usr/bin/env python3

#----- tuple
x = ("denmark", "Finland", "Norway", "Sweden") # tuple
print(x)
x = ("denmark") # not a tuple
print(x)
x = ("denmark",) # tuple
print(x)

#------ lists
l =["zebra", 49, -879, "mouse", 200]
print(l)

#----- functions
print(len(("one",))) # output 1, without brackets prints num of letter
print(len([3,5,1,2,"pause",5]))
print(len("automatic"))


l.append("next")
print(l)
list.append(l, "extra") # alternative, legacy different
print(l)

#----- list editing
print(l[0])
l[1] = "fourty nine" # possible only on list, not for tuples
print(l)
