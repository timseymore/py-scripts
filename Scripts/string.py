# -*- coding: utf-8 -*-
"""
String

collection of string related functions


Created on Sat May  2 19:05:23 2020

@author: Tim
"""


# return copy of given list of strings with suffix appended to each string
def string_append (strings: list, suffix: str) -> list:
    temp = []
    for s in strings:
        temp.append((s + suffix))
    return temp



# Test Cases

suffix = ".jpg"        
lst1 = ["tim", "star", "brooke"]
lst2 = string_append(lst1, suffix)

# print the new list with suffix
print(lst2)
  
# here we can see that the original list has not been mutated     
print(lst1)
