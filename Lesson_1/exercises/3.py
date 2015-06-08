#!/usr/bin/env python3

import random

pronoun  = ("my", "yours", "her", "his")
subject = ("cat", "dog", "man", "woman")
verb = ("sings", "runs", "jumps")
adverb = ("loudly", "quietly", "quality", "awfully")

for i in [1,2,3,4,5]:
        print(
            random.choice(pronoun),
            random.choice(subject),
            random.choice(verb),
            random.choice(adverb))
