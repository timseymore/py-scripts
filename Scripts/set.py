# -*- coding: utf-8 -*-
"""
Sets

numerical sets and operations on them

Created on Tue May 19 20:08:17 2020

@author: Tim
"""

test_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

def set_mod_2_3(size):
    temp = {}
    index = 0
    for i in range(1, size + 1):
        if (i % 2 == 0) or (i % 3 == 0):
            temp[index] = i
            index += 1
    return temp

set1000 = set_mod_2_3(1000)



    