# -*- coding: utf-8 -*-
"""
Even Permutation for 15-Puzzle

To solve a 15-puzzle we must first check that the given permutation is even.

Is the permutation [0,3,2,4,5,6,7,1,9,8] even?

Created on Sat May 16 15:06:09 2020

@author: Tim
"""

def is_permutation(p):
    return (set(p)==set(range(len(p))))


def is_even(p):
    count = 0    
    for i in range(len(p)):
        cursor = p[i]
        pos = i        
        while pos > 0 and p[pos - 1] > cursor:
            # Swap the number down the list
            p[pos] = p[pos - 1]
            pos -= 1
            count += 1
        # Break and do the final swap
        p[pos] = cursor
    return count % 2 == 0
    
    


# Tests
      
print (is_permutation([0]) == True)
print (is_permutation([0,2,1]) == True)
print (is_permutation([1,2,3]) == False)
print (is_permutation([0,1,2,3]) == True)

print(is_even([0]) == True)
print(is_even([0,3,2,4,5,6,7,1,9,8]) == True)
print(is_even( [1, 3, 8, 4, 5, 6, 9, 2, 0, 7]) == False)

