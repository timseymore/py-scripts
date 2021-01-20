# -*- coding: utf-8 -*-
"""
Curry

example of a curried function python


Created on Fri May  8 20:20:39 2020

@author: Tim
"""


curried_dec = lambda fn, x: fn(x)

curried_add = lambda x: lambda y: x + y



# Test Cases

result1 = curried_dec(len, "hi")
result2 = curried_add(2)(5)

# print(result1) 
