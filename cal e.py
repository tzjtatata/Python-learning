# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 10:47:09 2014

@author: Yuanze LEO
"""
#make factorial funciton
from math import *
i = 0
total = 0
k = 1/float(factorial(i))
while float(k) >=0.000001:
    total += k
    i += 1
    k =1/float(factorial(i))
#print total
print format(total,'.5f')
