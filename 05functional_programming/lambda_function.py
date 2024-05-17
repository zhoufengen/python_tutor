#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
匿名函数：
在Python中，对匿名函数提供了有限支持。
关键字lambda表示匿名函数，冒号前面的x表示函数参数。
匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
""")

def is_odd(n):
    return n % 2 == 1

L = list(filter(lambda n: n%2 == 1, range(1, 20)))

print("L=", L)