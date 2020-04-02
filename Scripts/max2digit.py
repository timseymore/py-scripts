# -*- coding: utf-8 -*-
"""
Max 2-digit integers


Created on Thu Apr  2 10:25:42 2020

@author: tim_s
"""

def build_num_lst(x, y):
    num_lst = []
    for i in range(x, y+1):
        num_lst.append(i)
    return num_lst

# TODO: use backtracking to find check all permutations
def sum_under_hundred(lst):
    ans_lst = []
    for i in lst:
        for j in ans_lst:
            if i + j != 100:
                ans_lst.append(i)
    return ans_lst

# print(build_num_lst(10, 99))
print(sum_under_hundred(build_num_lst(10, 99)))
