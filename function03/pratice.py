#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

logging.basicConfig(level=logging.DEBUG)

print("函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积:")
def mul(x, y):
  return x * y

print("mul(2, 3)=", mul(2, 3))


print("写一个函数，传入的参数可以是1个，或者多个，如果传入1个参数，则返回参数本身，如果传入多个参数，则返回多个参数的乘积，没有参数就抛出TypeError异常:")

def mul(a, *args):
  if len(args) == 0:
    return a
  else:
    return a * mul(*args)

print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('测试失败!')
elif mul(5, 6) != 30:
    print('测试失败!')
elif mul(5, 6, 7) != 210:
    print('测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        mul()
        print('测试失败!')
    except TypeError as e:
        logging.exception("Caught Exception: %s", e)
        print('测试成功!')
