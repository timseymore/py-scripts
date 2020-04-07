# -*- coding: utf-8 -*-
"""
Change


Changes any monetary amount greater than 24 using coins of value 7 or 5 only


Created on Mon Apr  6 19:36:49 2020

@author: Tim
"""

def change(n):
    assert(n >= 24)
    if n == 24: 
        return [5,5,7,7]
    if n == 25: 
        return [5,5,5,5,5]
    if n == 26: 
        return [5,7,7,7]
    if n == 27: 
        return [5,5,5,5,7]
    if n == 28: 
        return [7,7,7,7]

    coins = change(n - 5)
    coins.append(5)
    return coins
