#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created by zhouFe

"""
print("dict的key迭代：")
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

print("dict的value迭代：")
for value in d.values():
    print(value)

print("dict的key和value一起迭代：")
for key, value in d.items():
    print(key, value)


print("如何判断一个对象是可迭代对象呢？方法是通过collections.abc模块的Iterable类型判断:")
from collections.abc import Iterable
print("isinstance('abc', Iterable)=", isinstance('abc', Iterable))

print("Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身:")
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

print("同时引用了两个变量，在Python里是很常见的:")
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


print("请使用迭代查找一个list中最小和最大值，并返回一个tuple:")
def findMinAndMax(L):
    if len(L) > 0:
        min = L[0]
        max = L[0]
        for i in L:
            if i < min:
                min = i
            if i > max:
                max = i
        return (min, max)
    return (None, None)


print("findMinAndMax([7, 1, 3, 9, 5])=", findMinAndMax([7, 1, 3, 9, 5]))

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
