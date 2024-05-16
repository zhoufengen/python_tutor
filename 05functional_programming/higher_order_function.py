#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
logging.basicConfig(level=logging.INFO)

print("一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数")

print("变量可以指向函数:")
f = abs
print("f(-10)=", f(-10))

print("函数名也是变量")
try:
    abs = 10
    print("abs(-10)=", abs(-10))
except Exception as e:
  logging.exception("Caught Exception: %s", e)
print("要恢复abs函数，请重启Python交互环境。")

def add(x, y, f):
    return f(x) + f(y)

#f = lambda x: x * x
f = lambda x: x + x

print("add(5, 6, f)=", add(5, 6, f))

import builtins
abs = builtins.abs

print("add(5, 6, abs)=", add(5, 6, abs))

