# -*- coding: utf-8 -*-
"""
Curry

example of a curried function python


Created on Fri May  8 20:20:39 2020

@author: Tim
"""


curried_fun = lambda fn, x: fn(x)

curried_add = lambda x: lambda y: x + y

# Test Cases
# result = curried_fun(len, "hi")
result = curried_add(2)(5)

print(result) 
