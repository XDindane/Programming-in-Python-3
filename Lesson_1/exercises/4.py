#!/usr/bin/env python3

import random

pronoun  = ("my", "yours", "her", "his")
subject = ("cat", "dog", "man", "woman")
verb = ("sings", "runs", "jumps")
adverb = ("loudly", "quietly", "quality", "awfully")

default = 5

while True:
    try:
        line = input("enter number between 1 and 10: ")
        if 1 < int(line) < 10:
            default = int(line)
            break
        else:
            print("out of range")
            continue
    except ValueError as err:
        print(err)

                 
while default:
        print(
            random.choice(pronoun),
            random.choice(subject),
            random.choice(verb),
            random.choice(adverb))
        default -= 1
