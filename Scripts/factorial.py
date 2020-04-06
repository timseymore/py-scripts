# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 18:49:51 2020

@author: Tim
"""

# Iterative version of factorial
def fact0(n):
    assert(n > 0)
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
