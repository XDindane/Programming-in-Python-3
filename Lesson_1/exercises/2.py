#!/usr/bin/env python3

numbers = []
sumary = 0
while True:
    try:
        line = input("Enter number or press enter to end: ")
        numbers.append(int(line))
        sumary +=  int(line)
    except ValueError:
        break;
        
print("numbers: ", numbers)
print("count: ", len(numbers), "sum: ", sumary, "minimum: ", min(numbers), "maximum: ", max(numbers), "average: ", sumary / len(numbers))
