# -*- coding: utf-8 -*-
"""

Points and Vectors

modeling and working with points and vectors


Created on Thu May 21 16:04:45 2020

@author: Tim
"""

import matplotlib.pyplot as plt

from math import sqrt



class Plotable:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def plot(self, format='bo'):
        plt.plot(self.x, self.y, format)
        
    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + "]"
    

class Point(Plotable):
        
    def dist_to_origin(self):
        return sqrt(self.x  * self.x + self.y * self.y)


class Vector(Plotable):   
        
    def __add__(self, v):
        return Vector(self.x + v.x, self.y + v.y)
    
    def __mul__(self, n):
        return Vector(n*self.x, n*self.y)
    



# Test Cases
        
I_HAT = Vector(1, 0)
J_HAT = Vector(0, 1)

V1 = Vector(-1, 2)
V2 = Vector(2, 4)
V3 = Vector(1, 2)
V4 = Vector(3, -1)

V5 = V1 + V2
V6 = V3 + V4
V7 = V1 + V3

V8 = V1 * 2
V9 = V7 * 5
