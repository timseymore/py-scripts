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
    # check that given permutation is valid 
    if is_permutation(p):
        
        # recursively sort the given permutation,
        # keeping count of transpositions
        def aux(p1, index, acc):
            if p1 == []:
                return (acc % 2) == 0                
            else:    
                if index != p1[0]:
                    # it is incorrect
                    # swap (pi[0] and p1[1])
                    aux(p1, index, acc + 1)
                else:
                    # it is correct
                    # recursively sort rest of list
                    aux(p1[1::], index + 1, acc)
        
        return aux(p,0,0)
    else: 
        return False
    
    

 

# Tests
      
print (is_permutation([0]) == True)
print (is_permutation([0,2,1]) == True)
print (is_permutation([1,2,3]) == False)
print (is_permutation([0,1,2,3]) == True)

print(is_even([0]) == True)
print(is_even([0,2,1]) == True)
print(is_even([0,1,2,3]) == True)
print(is_even([0,3,2,1]) == True)
