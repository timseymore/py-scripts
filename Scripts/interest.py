# -*- coding: utf-8 -*-
"""
You have $1000 on day 11, and every day you earn 10\%10% of what you already get,
so that on day 22 you have $1000+10%⋅$1000=$1100, and on day 33 you have $1100+10%⋅$1100=$1210.
 On which day you will have more than $1000000 for the first time?
 Feel free to use the notebook about Bernoulli's inequality that we provided in this lesson.
Created on Thu Apr 16 17:42:39 2020

@author: Tim
"""


# %matplotlib inline

import matplotlib.pyplot as plt
import numpy as np


# You can play with the range of values for n and with the base 1.02, see what changes
sample = 200
x = np.arange(sample)
# This is used to plot the graph of 1.02^n, it is blue on the picture below
y = 1.02 ** x
plt.plot(x, y)
plt.xlabel('n')
plt.ylabel('Money($)')
# This is used to plot the graph of 1 + 0.02 * n, it is green on the picture below
z = 1 + 0.02 * x
plt.plot(x, z)
plt.show()


# Computes how much money you will have on day *day*, if you start with *starting_amount* of cash
# and earn *earn_percent* percents of what you already have every day.
def HowMuchMoney(starting_amount, earn_percent, day):
    day_multiplier = 1 + (earn_percent / 100.0)
    return starting_amount * (day_multiplier ** (day - 1))
    
def PrintExample(starting_amount, earn_percent, day):
    print("If you start with $%d and earn %d%% each day, you will have more than $%.0f on day %d!" % 
          (starting_amount, earn_percent, HowMuchMoney(starting_amount, earn_percent, day), day))




# Prints what will happen by day 74 if you start with $1000 and earn 10% every day
# Feel free to play with the parameters

# PrintExample(1000, 10, 74)
