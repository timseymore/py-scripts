# -*- coding: utf-8 -*-
"""
Combinatorics

Created on Sat May 30 17:57:36 2020

@author: Tim
"""

import itertools as it

# Rule of Sum:
# ------------
# If there are n objects of the first type and
# k objects of the second type, then there are
# n + k objects of one of the two types.

A = ['Alice', 'Bob', 'Charlie']
B = [0, 1, 2, 3]
C = A + B
print("Rule of Sum")
print(A)
print(B)
print(C)
print("Objects: " + str(len(C)))


# Rule of Product:
# ----------------
# If there are n objects of the first type and
# k objects of the second type, then there are
# n * k pairs of objects, the first of the 
# first type and the second of the second type.

D = ['a', 'b']
E = [1, 2, 3]
F = list(it.product(D, E))
print("Rule of Product")
print(D)
print(E)
print(F)
print("Pairs: " + str(len(F)))


# Tuples:
# -------
# The number of sequences of length k
# composed out of n symbols is n^k

print("Tuples")
print("'01' : n = 2, k = 6")
l = []
for p in it.product("01", repeat=6):
    print("".join(p))
    l.append(p)

print(" 2^6 = " + str(len(l)) + " total sequences")


# number of bitstrings of length 6 with equal 0 and 1 

l2 = []
count = 0
scount = 0
for bitstring in l:
    for bit in bitstring:
        if bit == '0':
            count += 1
        
    if count == 3:
        l2.append(bitstring)
        print(bitstring)
        scount += 1
    count = 0
    
print("length: " + str(scount))



# Pascal's Triangle:
# ------------------

print("Pascal's Triangle: 7 choose 4")
choose = dict()  # dct([n,k]) is equal to n choose k
choose_range = 20
for n in range(choose_range):
    choose[n, 0] = 1
    choose[n, n] = 1    
    for k in range(1, n):
        choose[n, k] = choose[n - 1, k - 1] + choose[n - 1, k]        
print(choose[7,4])


# Salads
# ------
# how many combinations of three ingreidients 
# can we use to make a four item salad?
print("Salads with tomato, bell pepper, and/or lettuce")
for c in it.combinations_with_replacement("TBL", 4):
    print("".join(c))
