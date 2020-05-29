# -*- coding: utf-8 -*-
"""
Connections

calculate the number of connections between n nodes

Created on Fri May 29 08:33:15 2020

@author: Tim
"""

from itertools import combinations

for c in combinations("abcdefgh", 2):
    print("".join(c))
    
def count_connections (n, t):
    connections = []
    for c in combinations(n,t):
        connections.append(c)
    return len(connections)


print (count_connections("abcdefgh", 2))

# recusively

def t(n):
    if n <= 1:
        return 0
    return (n-1) + t(n-1)

