#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

logging.basicConfig(level=logging.DEBUG)

print("如果一个函数在内部调用自身本身，这个函数就是递归函数。")
print("计算阶乘，用递归的写法：")

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print("fact(5)=", fact(5))

try:
  fact(1000)
except Exception as e:
  logging.exception("Caught Exception: %s", e)


print("""解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。
尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
""")

def fact(n):
    return fact_iter(n, 1)
def fact_iter(n, product):
    if n == 1:
        return product
    return fact_iter(n - 1, n * product)

try:
  fact(1000)
except Exception as e:
  logging.exception("22222 Caught Exception: %s", e)

print("遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。")


