#!/usr/bin/env python3

x = "blue"
y = "green"
z = x

print(x,y,z) #prints blue, green, blue

z = y

print(x,y,z) #prints blue, green, green

x = z
print(x,y,z) #prints green, green, green


#----------
route = 866
print(route, type(route))

route = "north"
print(route, type(route))
