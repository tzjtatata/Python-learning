# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 13:11:44 2014

@author: Yuanze LEO
"""

def do_n(n):
    if n!=0:
        do_n(n-1)

n = eval(raw_input("input n:"))
do_n(n);