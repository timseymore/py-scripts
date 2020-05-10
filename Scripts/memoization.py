# -*- coding: utf-8 -*-
"""
Memoization

uses and practice memoization in python


Created on Fri May  8 20:13:29 2020

@author: Tim
"""


def memo_map (fn: callable, xs: list) -> list:
    def aux (acc: list, cache: dict) -> list:
        for x in xs: 
            if x in cache.keys():
                ans = cache[x]
            else:
                ans = fn(x)
                cache[x] = ans
            acc.append(ans)
        return acc
    return aux([], {})

    
    
# Test Cases
    
zs = [1, 2, 3, 3, 4, 2, 6, 8, 6, 8]
result1 = memo_map(lambda x: x ** x, zs)
result2 = memo_map(lambda x: 2, zs)

# print(result2)
