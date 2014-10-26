# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 12:57:35 2014

@author: Yuanze LEO
"""
from math import *
x1,y1 = eval(raw_input("input x1,y1: "))
x2,y2 = eval(raw_input("input x2,y2: "))
x3,y3 = eval(raw_input("input x3,y3: "))
a = sqrt((x2-x3)**2 + (y2-y3)**2)
b = sqrt((x1-x3)**2 + (y1-y3)**2)
c = sqrt((x2-x1)**2 + (y2-y1)**2)
A = acos((a*a -b*b -c*c) / (-2 *b*c))
B = acos((-a*a +b*b -c*c) / (-2 *a*c))
C = acos((-a*a -b*b +c*c) / (-2 *b*a))
print "A =",A
print "B =",B
print "C =",C