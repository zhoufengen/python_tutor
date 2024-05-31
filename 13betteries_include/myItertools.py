#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce

print("""
Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。

count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列：
cycle()会把传入的一个序列无限重复下去：
repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
takewhile()等函数根据条件判断来截取出一个有限的序列：
chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
groupby()把迭代器中相邻的重复元素挑出来放在一起：
实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key。如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：
""")
# import itertools
# natuals = itertools.count(1)
# for n in natuals:
#     print(n)

# import itertools
# cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
# for c in cs:
#     print(c)

# import itertools
# ns = itertools.repeat('A', 3)
# for n in ns:
#     print(n)

import itertools
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

for c in itertools.chain('ABC', 'XYZ'):
    print(c)

for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))


for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))

#创建一个奇数序列
# ns = itertools.count(1, 2)
# for n in ns:
#     print(n)


print("""
计算圆周率：
""")


def divi4(x):
    if index % 2 == 0:
        return 4 / x
    return -4 / x

#计算圆周率
def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9,
    ns = itertools.count(1, 2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    ns = itertools.islice(ns, N)
    nsl = enumerate(ns)    #生成带下标的list
    #print("nsl=", nsl)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9,
    #1, 3, 5, 7, 9 变成 4/1, -4/3, 4/5, -4/7, 4/9 用列表生成式转换一下：
    transformed_sequence = [(4 / i) if (n % 2 == 0) else -(4 / i) for n, i in nsl]
    #print("transformed_sequence=", transformed_sequence)
    # step 4: 求和:
    return reduce(lambda x, y: x + y, transformed_sequence)


# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')

