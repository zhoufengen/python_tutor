#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("通过循环绘制5个五角星：")

from turtle import *

def drawStar(x, y):
    pu()       # pen up
    goto(x, y) # move to x, y
    pd()       # pen down
    # set heading: 0
    seth(0)    # set heading: 0
    for i in range(5):
        fd(40) # forward 40
        rt(144) # right 144

for x in range(0, 250, 50): # 0, 50, 100, 150, 200
    drawStar(x, 0)

done()
