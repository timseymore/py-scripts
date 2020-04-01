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
    valids = []
    for perm in it.permutations(range(n)):
        if is_solution(perm):
            valids.append(perm)
            print(perm)
    print(valids.__len__())
    
    
find_solution(8)   
     

# Backtracking method

def can_be_extended_to_solution(perm):
    i = len(perm) - 1
    for j in range(i):
        if i - j == abs(perm[i] - perm[j]):
            return False
    return True

def extend(perm, n):
    if len(perm) == n:
        print(perm)
        exit()

    for k in range(n):
        if k not in perm:
            perm.append(k)

            if can_be_extended_to_solution(perm):
                extend(perm, n)

            perm.pop()

# extend(perm = [], n = 13)