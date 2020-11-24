# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 11:07:49 2020

@author: Tim
"""

# caluculate the Future Value of a Lump Sum amount
def fv(pv, r, n):
    return pv * ((1 + r)**n)

# calculate the Present Value of a Future Lump Sum
def pv(fv, r, n):
    return fv / ((1 + r)**n)
    