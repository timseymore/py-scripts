# -*- coding: utf-8 -*-
"""
n queens puzzle solution checker


"""

import itertools as it


# Brute Force method

def is_solution(perm):
    for (i1, i2) in it.combinations(range(len(perm)), 2):
        if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
            return False
    return True


def find_solution(n):
    for perm in it.permutations(range(n)):
        if is_solution(perm):
            print(perm)
            return
    
    
find_solution(8)   
     