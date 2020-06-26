# -*- coding: utf-8 -*-
"""
Probability


Created on Fri Jun 26 11:30:03 2020

@author: Tim
"""

import random
import itertools

# Tossing a coin 100,000 times and checking how many 
# heads flips there are versus tail flips,
# we can see that about half the tosses land heads.
# Notice that the larger the number of flips, the closer to .50 we get.
flips = 100000
heads = 0
tails = 0
for i in range (flips):
    x = random.choice(["heads", "tails"])
    if x == "heads":
        heads += 1
    else:
        tails += 1        
print("Heads: " + str(heads))
print("Tails: " + str(tails))
print("Frequency of heads: " + str(heads / flips))



