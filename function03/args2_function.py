#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.DEBUG)

print("**********************3.可变参数***************************")
print("可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。")
print("计算a的2次方+b的2次方+c的2次方......")

def calc(*numbers):
  sum = 0
  print("tuple nums=", numbers)
  for n in numbers:
    sum += n * n
  return sum

nums = [1,2,3]
print("nums = [1,2,3]调用可变参数的两种方式1:calc(nums[0], nums[1], nums[2])=", calc(nums[0], nums[1], nums[2]))
print("nums = [1,2,3]调用可变参数的两种方式2:calc(*nums)=", calc(*nums))
print("传入0个参数calc()=", calc())
print("*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。")

print("**********************4.关键字参数***************************")
print("""可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict.""")
def persion(name, age, **kw):
  if 'job' in kw:
     kw['job'] = kw['job'] + '_modify_in_function'
  print("name=", name, "age=", age, "other=", kw)

print("call persion('jhon', 18, city='Guangzhou', gender='F')", persion('jhon', 18, city='Guangzhou', gender='F'))
print("试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。")
extraArgs = {"city": "Beijing", "job": "Engineer", "gender": "F"}
print("call persion('jhon', 18, **extraArgs)", persion('jhon', 18, **extraArgs))
print("**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra.")
print("extraArgs=", extraArgs)
print("可以传0个或者任意个关键字参数：persion('jhon', 18)========>", persion('jhon', 18))



print("**********************5.命名关键字参数***************************")
print("对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。")
print("如果要限制关键字参数的名字，就可以用命名关键字参数. ")

def person(name, age, *, city, job):
  print(name, age, city, job)

print("call person('jhon', 18, city'Beijing', job='Engineer')", person('jhon', 18, city='Beijing', job='Engineer'))

print("不能不穿命名关键字参数，否则会报错：")
try:
  print("call person('jhon', 18)", person('jhon', 18))
except Exception as e:
  logging.exception("Caught execption: %s", e)

print("传的命名关键字参数不符合命名关键字参数的规则city, job，会报错：")
try:
  print("call person('jhon', 18, gender='F')", person('jhon', 18, gender='F'))
except Exception as e:
  logging.exception("Caught Exception: %s", e)


print("和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。")
print("如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了")
def person(name, age, *args, city, job):
  print(name, age, args, city, job)

print("person('jhon', 18, 11, 22, city='Beijing', job='Engineer')=")
person('jhon', 18, 11, 22, city='Beijing', job='Engineer')

print("由于调用时缺少参数名city和job，Python解释器把前两个参数视为位置参数，后两个参数:'Beijing', 'Engineer'传给*args，但缺少命名关键字参数导致报错:")
try:
  person('jhon', 18, 'Beijing', 'Engineer')
except Exception as e:
  logging.exception("Caught Exception: %s", e)

print("命名关键字参数可以有缺省值，从而简化调用：")
def person(name, age, *, city='Beijing', job):
  print(name, age, city, job)

print("call persion('john', 18, 'Engineer')")
person('john', 18, job='Engineer')

print("**********************6.参数组合***************************")
print("在Python中定义函数，可以用位置参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：位置参数、默认参数、可变参数、命名关键字参数和关键字参数。")
print("所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。")
print(" 虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。")

