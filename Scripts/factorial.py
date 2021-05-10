# -*- coding: utf-8 -*-
"""
factorial.py

Two versions of factorial Functions


Created on Mon Apr  6 18:49:51 2020

@author: Tim
"""


# Iterative version
def fact0(n):
    assert(n > 0)
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Recursive version
def fact(n):
    assert(n > 0)
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)
