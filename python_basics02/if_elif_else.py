#!/usr/bin/env python3
# -*- coding: utf-8 -*-

age = 30

if age > 19:
   print("adult")
elif age > 70: 
   print("old")
else:
   print("teenager")


print("input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情:")
birthDate = input("Please input your Year of birth date:")
birth = int(birthDate)
if birth < 2000:
   print("00前")

else:
   print("00后")


