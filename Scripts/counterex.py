# -*- coding: utf-8 -*-
"""
Counterex

n2 + n + 41
Somebody has a conjecture: 
    
 for every integer n > 1 the number n 2 + n + 41 is prime 
 (is not a product of two smaller integers).
 
Is it true? If not, find a counterexample.


Created on Fri Apr 17 10:40:54 2020

@author: Tim
"""

    
def is_prime(n):
    divisor = 2
    result = True
    while divisor*divisor <= n:   
        if n % divisor == 0:
            result = False
            return
        divisor = divisor + 1
    return result



# Test Use
    
# for i in range(1, 100):
#     result = i**2 + i + 41
#     if not is_prime(result):
#         print(str(i) + ": " + str(result))
