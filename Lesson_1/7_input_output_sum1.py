#!/usr/bin/env python3

print("Enter numbers after each enter. For end enter empty value")

total = 0
count = 0

while True:
    line = input("číslo:") # if empty returns false to condition
    if line:
        try: # need catch exception for continue
            number = int(line)
        except ValueError as err:
            print(err)
        total += number
        count += 1
    else:
        break
if count:
    print("count: ", count, "total: ", total, "avarage: ", total / count)
