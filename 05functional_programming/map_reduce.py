#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
map函数的作用：
如果f（x）= x * x；把f(x)作用在list的每一个元素并把结果生成一个新的list
""")

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("list(map(lambda x: x * x, L))=", list(map(lambda x: x * x, L)))

f = lambda x: str(x) + "_" + str(x)
print("list(map(f, L))=", list(map(f, L)))


print("""
reduce函数的作用：
把一个函数作用在一个序列上，这个函数必须接收两个参数(x,y)，reduce把结果继续和序列的下一个元素做累积计算
""")

print("把一个字符串转换成整数：")

from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))


str_int = str2int('123456789')
print("str2int('123456789')=", str_int, type(str_int))


names = ['adam', 'LISA', 'barT', '' , '  ', 's']

def normalize(name):
    return name.capitalize()

# def normalize(name):
#     if not isinstance(name, str):
#         return name
#     if name is None:
#         return name
#     if len(name) == 0:
#         return name
#     if len(name) == 1:
#         return name.upper()
#     capitalize = name[0].upper() + name[1:].lower()
#     return capitalize

print("list(map(normalize, names))=", list(map(normalize, names)))