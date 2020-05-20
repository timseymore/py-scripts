# -*- coding: utf-8 -*-
"""

Counting

examples of counting and recursive counting used in cominatorics


We will be implementing a graph consisting of nodes
and then use recursive counting to find the number of
possible paths from the start node to any given node
in the graph.

The number of possible paths to any given node
is the sum of the possible paths to all of its sub-nodes.


Created on Wed May 20 17:58:07 2020

@author: Tim
"""


# We start by defining a simple node class.

class Node:
    def __init__(self, name: str, subs: list):
        self.name = name
        self.subs = subs
        

# We will now create nodes that will
# represent the structure of our graph.
# It is a one-directional graph, where each sub-node (child)
# has an arrow pointing to the parent node (self).
# Note that any given node may have any number of parent nodes.
        
N1 = Node("N1", [])
N2 = Node("N2", [N1])
N3 = Node("N3", [N1])
N4 = Node("N4", [N2, N3])
N5 = Node("N5", [N2, N4])
N6 = Node("N6", [N3])
N7 = Node("N7", [N5])
N8 = Node("N8", [N5, N7])
N9 = Node("N9", [N6, N7])
N10 = Node("N10", [N8, N9])


# Let's create a function to recursively count
# the number of possible paths from start (N1) to any given node n.
# This is poor style however, the function should be an inner method of Node.

def num_paths(n: Node):
    # We define an inner helper-function to recursively count.
    # Calling num_paths will be simpler without the need
    # to pass an accumulator, this will help avoid errors  
    # by ensuring the accumulator is always called starting at 0
    def aux(node, acc):
        if node.subs == []:
            # This is our base case: a node with no subs has one possible path
            return acc + 1
        else:
            # Sum the number of paths to each sub and return the result
            for sub in node.subs:                
                acc += aux(sub, 0)
            return acc
        
    return aux(n, 0)


# Some test cases to check that it works correctly
    
print(num_paths(N1) == 1)
print(num_paths(N2) == 1)
print(num_paths(N3) == 1)
print(num_paths(N4) == 2)
print(num_paths(N5) == 3)
print(num_paths(N6) == 1)
print(num_paths(N7) == 3)
print(num_paths(N8) == 6)
print(num_paths(N9) == 4)
print(num_paths(N10) == 10)
