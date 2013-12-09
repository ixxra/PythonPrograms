# -*- coding: utf-8 -*-
'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

import time
a=time.time()
numbers=[]
for i in range(999,99,-1):
    for z in range(i,99,-1):
        N=str(z*i)
        L=len(N)-1
        for p in range(L):
            if (N[p]==N[L-p])==False:
                break
            if 2*p>L and (N[p]==N[L-p])==True:
                M=int(N)
                numbers.append(M)
print max(numbers)
b=time.time()
print b-a
