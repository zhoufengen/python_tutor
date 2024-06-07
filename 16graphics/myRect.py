#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
在1966年，Seymour Papert和Wally Feurzig发明了一种专门给儿童学习编程的语言——LOGO语言，它的特色就是通过编程指挥一个小海龟（turtle）在屏幕上绘图。
海龟绘图（Turtle Graphics）后来被移植到各种高级语言中，Python内置了turtle库，基本上100%复制了原始的Turtle Graphics的所有功能。
我们来看一个指挥小海龟绘制一个长方形的简单代码：
""")

# 导入turtle包的所有内容:
from turtle import *

# 设置笔刷宽度:
width(10)

# 前进:
pencolor('yellow')
forward(200)
# 右转90度:
right(90)

# 笔刷颜色:
pencolor('red')
forward(100)
right(90)

pencolor('green')
forward(200)
right(90)

pencolor('blue')
forward(100)
right(90)

# 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
done()
