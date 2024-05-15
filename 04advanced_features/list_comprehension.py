#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。")

print("list 中的每个元素自己相乘，然后返回一个新的list：")
L = [1, 2, 3, 4, 5, 6]
M = [x * x for x in L]
print(M)

print("for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：")
N = [x * x for x in L if x % 2 == 0]
print(N)


print("列出当前目录下的所有文件和目录名，可以通过一行代码实现:")
import os
D = [d for d in os.listdir('../')]
print(D)


print("字典的key和value可以同时迭代: ")
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])

print("把一个list中所有的字符串变成小写：")
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

print("在列表生成式前面写if和后面写if的区别：后面的是筛选取元素，前面的是计算元素最终形成list元素：")
L = [1, 2, 3, 4, 5, 6]
M = [x if x % 2 != 0 else -x for x in L if x % 2 == 0]
print(M)


print("一个字符串和数字类型混合的列表，使用内置的isinstance函数可以判断一个变量是不是字符串，是就转换为大写：")
L = ['Hello', 49, 'World', 42, 'IBM', 3.142]
print([s.upper() if isinstance(s, str) else s for s in L])

