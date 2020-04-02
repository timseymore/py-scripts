# -*- coding: utf-8 -*-
"""
Max 2-digit integers

calculate how many 2-digit integers between 1-100 can be added to a list
so that no two numbers will add to 100

Created on Thu Apr  2 10:25:42 2020

@author: tim_s
"""


def build_num_lst(x: int, y: int) -> list:
    num_lst = []
    for i in range(x, y+1):
        num_lst.append(i)
    return num_lst


def check_num(n: int, lst: list) ->  bool:
    for i in lst:
        if n + i == 100:
            return False
    return True

def max2(lst: list, ans_lst: list) -> int:
    if lst == []:
        return len(ans_lst)
    elif ans_lst == [] or check_num(lst[0], ans_lst):
        ans_lst.append(lst[0])
    return max2(lst[1::], ans_lst)


# print(build_num_lst(10, 99))
print(max2(build_num_lst(10, 99), []))
