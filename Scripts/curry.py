# -*- coding: utf-8 -*-
"""
Curry

example of a curried function python


Created on Fri May  8 20:20:39 2020

@author: Tim
"""

curried_fun = lambda fn, x: fn(x)


# Test Uses
result = curried_fun(len, "hi")
print(result) # 2
