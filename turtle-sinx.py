# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 12:29:58 2014

@author: Yuanze LEO
"""
import turtle as tl
import math
tl.reset()
tl.up()
tl.pensize(1)
a = math.pi
x = -a*100
tl.goto(x,0)
tl.down()
tl.goto(-x,0)
tl.stamp()
tl.up()
tl.left(90)
tl.goto(0,x)
tl.down()
tl.goto(0,-x)
tl.stamp()
tl.penup()
tl.pensize(3)
tl.color('red')
tl.goto(x,0)
tl.pendown()
n = 100
m = 10   
i = 0
while i<=n:
    x = x+ a/m +2*a
    tl.goto(x,math.sin(x)*100)
    i += 1


