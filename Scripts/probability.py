# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:30:03 2020

@author: Tim
"""
import random
import itertools

count1 = 0
count0 = 0

for i in range (10000):
    x = random.choice([0,1])
    if x == 1:
        count1 += 1
    else:
        count0 += 1
print(abs(count1) - abs(count0))
    
    



outcomes = { 'heads':0,
             'tails':0,
             }
sides = outcomes.keys()

for i in range(10000):
    outcomes[ random.choice(sides) ] += 1

print ('Heads:', outcomes['heads'])
print ('Tails:', outcomes['tails'])