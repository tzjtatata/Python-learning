# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 12:29:58 2014

@author: Yuanze LEO
"""
import turtle as tl
import math
tl.reset()
tl.penup()
tl.pensize(3)
tl.color('red')
a = math.pi
x = -a*100
tl.goto(x,0)
tl.pendown()
n = 100
m = 10   
i = 0
while i<=n:
    x = x+ a/m +2*a
    tl.goto(x,math.sin(x)*100)
    i += 1
tl.color("black")
tl.up()
x = -a*100
tl.goto(x,math.cos(x))
n = 100
m = 10   
i = 0
tl.down()
while i<=n:
    x = x+ a/m +2*a
    tl.goto(x,math.cos(x)*100)
    i += 1


