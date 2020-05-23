# -*- coding: utf-8 -*-
"""

Vector

modeling and working with vectors


Created on Thu May 21 16:04:45 2020

@author: Tim
"""

class Vector:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def __add__(self, v):
        return Vector(self.x + v.x, self.y + v.y, self.z + v.z)
    
    def __mul__(self, n):
        return Vector(n*self.x, n*self.y, n*self.z)
    
    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "]"



I_HAT = Vector(1, 0)
J_HAT = Vector(0, 1)

V1 = Vector(-1, 2)
V2 = Vector(2, 4)
V3 = Vector(1, 2, 2)
V4 = Vector(3, -1, 3)


