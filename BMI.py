# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 13:05:34 2014

@author: Yuanze LEO
"""
import math
try:
    high = eval(raw_input("Please input your height(m):"))
    high = fabs(high)
    weight = eval(raw_input("Please input your weight(kg):"))
    weight = fabs(weight)
    BMI = weight/(high*high)
    if BMI >=29.9:
        print "Obese"
    elif BMI >=24.9:
        print "Overweight"
    elif BMI >=18.5:
        print "Normal"
    elif BMI>= 0:
        print "Underweight"
    else :
        print "Error"
except:
    print "Error"