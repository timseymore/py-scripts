# -*- coding: utf-8 -*-
"""
Memoization

uses and practice memoization in python


Created on Fri May  8 20:13:29 2020

@author: Tim
"""

def memo_map (fn, xs):
    def aux (ys, acc, mem):
        for y in ys: 
            if y in mem.keys():
                print("using cache on " + str(y))
                ans = mem[y]
            else:
                ans = fn(y)
                mem[y] = ans
            acc.append(ans)
        return acc
    return aux(xs, [], {})

    
    
# Test Cases
    
ts = [1, 2, 3, 3, 4, 2, 6, 8, 6, 8]
result = memo_map(lambda x: x ** x, ts)
print(result)