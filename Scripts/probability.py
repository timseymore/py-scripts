# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:30:03 2020

@author: Tim
"""
import random
import itertools

heads = 0
tails = 0

for i in range (10000):
    x = random.choice(["heads", "tails"])
    if x == "heads":
        heads += 1
    else:
        tails += 1
        
print("Heads: " + str(heads))
print("Tails: " + str(tails))
print("Probability of heads: " + str(abs(heads / tails)))

