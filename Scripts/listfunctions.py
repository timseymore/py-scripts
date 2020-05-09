# -*- coding: utf-8 -*-
"""
List functions
 
filter, map, and fold implementations


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


def myfold (f, lst, acc):
    for i in lst:
        acc = f(i,acc)
    return acc



# Test cases
    
testlist = [-4, -3, -2, -1, -0, 1, 2, 3, 4]


is_below_2 = lambda x: x < 2
    
is_positive = lambda x: x > 0

increment = lambda x: x + 1

negate = lambda x: x * -1

add = lambda x, y: x + y

multiply = lambda x, y: x * y


# print(myfilter(is_positive, testlist))
# print(myfilter(is_below_2, testlist))

# print(mymap(increment, testlist))
# print(mymap(negate, testlist))

# print(testlist[5:])
# print(myfold(add, testlist[5:], 0))
# print(myfold(multiply, testlist[5:], 1))
