# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 13:18:12 2014

@author: Yuanze LEO
"""

from math import *
def estimate_pi():
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        num = factorial(4*k) * (1103 + 26390*k)
        x = factorial(k)**4 * 396**(4*k)
        term = factor * num / x
        total += term
        if abs(term) < 1e-15: 
            break
        k += 1
    return 1 / total
print estimate_pi()