# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 17:47:59 2014

@author: Yuanze LEO
"""
def reverse(text):
    a = []
    k = len(text)
    for i in range(k,0,-1):
        a.append(text[i-1])
    return ''.join(a)

print reverse("Python!")