# -*- coding: utf-8 -*-
"""
List functions
 
filter, map, and fold

Created on Sat Apr 18 21:33:08 2020

@author: tim_s
"""


def myfilter (f, lst):
    result = []
    for element in lst:
        if f(element):
            result.append(element)
    return result


def mymap (f, lst):
    result = []
    for element in lst:
        result.append(f(element))
    return result


def fold (f, lst, acc):
    for i in lst:
        acc = f(i,acc)
    return acc



# Test code 
    
testlist = [-4, -3, -2, -1, -0, 1, 2, 3, 4]

def isbelowx (n, x):
    return n < x

def isbelow2 (n):
    return isbelowx(n, 2)
    
def ispositive (n):
    return n > 0

def increment (n):
    return n + 1

def negate (n):
    return n * -1

def add (x,y):
    return x + y

def multiply (x,y):
    return x * y



# print(myfilter(ispositive, testlist))
# print(myfilter(isbelow2, testlist))

# print(mymap(increment, testlist))
# print(mymap(negate, testlist))

# print(testlist[5:])
# print(fold(add, testlist[5:], 0))
# print(fold(multiply, testlist[5:], 1))



