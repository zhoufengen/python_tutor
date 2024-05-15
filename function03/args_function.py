#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.DEBUG)


print("**********1.位置参数*****************")
print("参数的名字和位置确定下来的参数叫位置参数")

def power(x):
  return x * x

print("计算x的2次方:power(3)=", power(3))
print("计算x的3次方,4次方,5次方等等,不重新定义函数能不能办到?")
print("能!可以把power(x)修改为power(x, n)，用来计算x的n次方!")

def power(x, n):
  result = 1
  while n > 0:
    n = n - 1
    result = result * x
  return result

print("power(2, 2)=", power(2, 2), "power(2, 3)=", power(2, 3), "power(2, 4)=", power(2, 4), "power(2, 5)=", power(2, 5))

print("**********2.默认参数*****************")
print("有默认值的参数")
print("有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数")
print("默认参数降低了函数调用的难度")
try:
  print("power(3)=", power(3))
except Exception as e:
  logging.exception("Caught exception: %s", e)    

print("因为power函数加了位置参数n, 调用的时候没传, 函数不知道怎么处理, 所以报错了! 有没有办法兼容这种情况呢?")
print("有!!!使用默认参数: 如果没传n就给个默认值, 传了就使用传入的值!")

def power(x, n=2):
  result = 1
  while n > 0:
    n = n - 1
    result = result * x
  return result

print("这时调用就不会报错:power(3)=", power(3))

print("例如小学入学的登记函数, 只需要名字和性别就可以了:")
def enroll(name, gender):
   print("name=", name, "gender=", gender)
 
print("enroll('Sarah', 'F')=")
enroll('Sarah', 'F')

print("但是有时候也需要额外的信息:年龄和城市, 就可以设置他们为默认参数:不传就默认,传就使用传的值:")

def enroll(name, gender, age=6, city='Beijing'):
   print("name=", name, "gender=", gender, "age=", age, "city=", city)


print("不传入age和city=")
enroll('Sarah', 'F')
print("传入age和city=")
enroll('Sarah', 'F', 7, 'Shanghai')

print("默认参数有个最大的坑: 定义的函数,参数是list, 给默认值为空[]:def add_end(L=[])")
def add_end(L=[]):
    L.append('END')
    return L

print("传入list=[1,2,3,4]调用是正确的add_end([1,2,3,4]):", add_end([1,2,3,4]))
print("默认参数调用时,第1次是正确的add_end()", add_end())
print("默认参数调用时,第2+次是错误的add_end()", add_end())
print("所以定义默认参数要牢记一点：默认参数必须指向不变对象！")
print("可以用None这个不可变对象来改造def add_end(L=None):")
def add_end(L=None):
    if L is None:
       L = []
    L.append('END')
    return L

print("传入list=[1,2,3,4]调用是正确的add_end([1,2,3,4]):", add_end([1,2,3,4]))
print("默认参数调用时,第1次是正确的add_end()", add_end())
print("默认参数调用时,第2+次是正确的add_end()", add_end())
