# -*- coding: utf-8 -*-
"""

Using bisection search to approximate square root

Created on Thu Feb  1 21:29:30 2018

@author: tim_s
"""
def sqrt(x):
    
    x = -25
    x = abs(x)
    epsilon = .01
    numGuesses = 0
    low = 0.0
    high = max(1.0, x)
    ans = (high + low)/2.0
    while abs(ans**2 - x) >= epsilon:
        print('low = ', low, 'high = ', high, 'ans =', ans)
        numGuesses += 1
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = abs(high + low)/2.0
    print('numGuesses = ', numGuesses)
    print(ans, 'is close to the square root of ', x)
