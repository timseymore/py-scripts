# -*- coding: utf-8 -*-
"""
Change


Changes any monetary amount greater than 8 using coins of value 3 or 5 only


Created on Mon Apr  6 19:36:49 2020

@author: Tim
"""

def change(n):
    assert(n >= 8)
    if n == 8: 
        return [3,5]
    if n == 9:
        return [3,3,5]
    if n == 10:
        return [5,5]
    
    coins = change(n - 3)
    coins.append(3)
    return coins
