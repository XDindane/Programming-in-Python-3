#!/usr/bin/env python3

import random

numbers = []
indexes = []
total = 0
lowest = None
highest = None

while True:
    try:
        line = input("enter number or press enter to end: ")
        if not line:
            break
        indexes.append(len(numbers)) # indexes for loop in sorting
        number = int(line)
        numbers.append(number)
        total += number
        if lowest is None or lowest > number:
            lowest = number
        if highest is None or highest < number:
            highest = number
    except ValueError as err:
        print(err)

numLength = len(numbers)
print("numbers:", numbers)
print("count =", numLength, "sum =", total,
      "minimum =", lowest, "maximum =", highest,
      "average =", total / numLength)


# sorting
repeat = True
while repeat: # repeat
    repeat = False
    for i in indexes: # can't use while cycle. 
        if i+1 == numLength:
            break
        if numbers[i] > numbers[i+1]: # if first is bigger than second
            prev = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = prev
            repeat = True 
        
# median
middle = int(len(numbers)/2)
median = numbers[middle]
if middle and middle * 2 == len(numbers):
    median = (median + numbers[middle -1] / 2)
print("median", median)
