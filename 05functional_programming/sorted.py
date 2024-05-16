#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("利用sorted()对数字自然排序：")
print(sorted([36, 5, -12, 9, -21]))
print("利用sorted()对数字的绝对值排序：")

print("sorted 中的key就是对排序对象的处理，然后再进行排序")
print(sorted([36, 5, -12, 9, -21], key=abs))

print("利用sorted()对字符串ASCII码自然排序：")
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print("利用sorted()对字符串ASCII码的忽略大小写排序：")
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

print("利用sorted()对字符串ASCII码的忽略大小写反向排序：")
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

print("用一组tuple表示学生名字和成绩")
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print("利用sorted()按学生成绩排序：")
def by_score(t):
    return t[1]
print("sorted(L, key=by_score)=", sorted(L, key=by_score))

by_name = lambda t: t[0].lower()
print("sorted(L, key=by_name)=", sorted(L, key=by_name))

