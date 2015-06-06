#!/usr/bin/env python3

#--- operator identity
a = ["retence",3,None]
b = ["retence",3,None]
print(a is b) # false
b = a
print(a is b) # true,
#very fast. Compares only memory object adress not objects
a = "something"
b = None
print(a is not b) # true
print(b is None) # true


#--- comparision operators
a = 2
b = 6
print (a == b) # false
print (a < b) # true
print (a <= b, a != b, a >= b, a > b) # true, true, false, false

a = "many routes"
b = "many routes"
print(a is b) #false,
#sometimes returns true. This is made for better efectiveness by python itself.
# operator of identity should use only for comparison with object None

print(a == b) #true

#chaining, the beutifull thing from python
a = 9
print (0 <= a <= 10)

#--- operator of authority(příslusnosti)
p = (4, "frog", 9,-33,9,2)
print(2 in p) #true
print("dog" not in p) #true

phrase = "multicolored calc"
print ("c" in phrase) #true
print("color" in phrase) #true


# --- logical operators (and, or, not)
five = 5
two = 2
zero = 0
print (five and two) #return Two
print(two and five) #return five
print (five and zero) # return zero

print (five or two) #return Two
print(two or five) #return five
print (five or zero) # return zero

#not = negative
nought = 0
print (not(zero or nought))







