
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def my_abs(num):
   if num > 0:
     return num
   else:
     return -num



print("调用自定义的函数my_abs(-100)=", my_abs(-100))



print("可以用pass定义一个空函数")
def nop():
  pass

print("call nop()=", nop())


print("数据类型检查可以用内置函数isinstance()实现")
def my_absII(num):
   if not isinstance(num, (int, float)):
      raise TypeError("参数类型不对!")
   return my_abs(num)

print("my_absII(-10000)=", my_absII(-10000))
#print("my_absII('ABC')=", my_absII('ABC'))

print("""
Python函数返回的仍然是单一值
原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
""")


def multipleReturn(x, y):
    return "精度" + str(x), "纬度" + str(y)


print("multipleReturn(110, 112)=", multipleReturn(110, 112))
xInfo, yInfo = multipleReturn(110, 112)
print("xInfo=", xInfo, "yInfo=", yInfo)
