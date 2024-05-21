#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import types

print("""
type()函数：
获取对象的类型：type()
""")

def fn():
    pass

print("type(fn)=", type(fn))
print("type(123)=", type(123))
print("type('123')=", type('123'))

print("""
使用types模块中定义的常量:
""")

print("type(fn) == types.FunctionType=", type(fn) == types.FunctionType)
print("type(abs) == types.BuiltinFunctionType=", type(abs) == types.BuiltinFunctionType)
print("type(lambda x: x)==types.LambdaType=", type(lambda x: x) == types.LambdaType)
print("type((x for x in range(10)))==types.GeneratorType=", type((x for x in range(10))) == types.GeneratorType)

print("""
isinstance()函数:
要判断class的类型，可以使用isinstance()函数:
""")

class Animal(object):
    pass

class Dog(Animal):
    pass

class Husky(Dog):
    pass

class Cat(Animal):
    pass

dog = Dog()
husky = Husky()

print("isinstance(dog, Dog)=", isinstance(dog, Dog))
print("isinstance(dog, Animal)=", isinstance(dog, Animal))

print("isinstance(husky, Husky)=", isinstance(husky, Husky))
print("isinstance(husky, Dog)=", isinstance(husky, Dog))
print("isinstance(husky, Animal)=", isinstance(husky, Animal))

print("isinstance(dog, Husky)=", isinstance(dog, Husky))

print("总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。")

print("""
dir()函数:
要获得一个对象的所有属性和方法，可以使用dir()函数:"
""")

class MyDir(object):
    def __init__(self):
        self.x = 100
        self.y = 200

    def __len__(self):
        return 100

    def power(self):
        return self.x * self.y


myDir = MyDir()

print("仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态:")
print("dir(myDir)=", dir(myDir))
print("hasattr(myDir, 'x')=", hasattr(myDir, 'x'))
print("getattr(myDir, 'x')=", getattr(myDir, 'x'))
setattr(myDir, 'x', 1000)
print("post setattr(myDir, 'x', 1000) getattr(myDir, 'x')=", getattr(myDir, 'x'))

print("有没有power方法：")
print("hasattr(myDir, 'power')=", hasattr(myDir, 'power'))
power = getattr(myDir, 'power')
print("判断power是个类方法isinstance(power, types.MethodType)=", isinstance(power, types.MethodType))
print("power()=", power())




