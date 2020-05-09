# -*- coding: utf-8 -*-
"""
Hanoi Towers

how many turns to solve a Hanoi towers puzzle with n discs


Created on Wed Apr  8 16:54:52 2020

@author: Tim
"""


def turns_to_solve(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return (turns_to_solve(n-1) * 2) + 1
    