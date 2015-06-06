#!/usr/bin/env python3

print("enter a file sum2.dat as source data")

total = 0
count = 0

while True:
    try: # need catch exception for continue
        line = input()
        if line:
            number = int(line)
            total += number
            count += 1
    except ValueError as err:
        print(err)
        continue
    except EOFError:
        break
    
if count:
    print("count: ", count, "total: ", total, "avarage: ", total / count)
