# -*- coding: utf-8 -*-
a = 1
t_007 = 'T007'
Answer = True
print(a, t_007, Answer)
x = 2
x = x + 2
print("x=", x)

a = 'ABC'
print("a='ABC' 1.内存中创建了一个对象ABC 2.内存中创建a变量,指向'ABC'")
print("a=", a)
b = a
print("b=a 3.内存中创建b变量,指向a变量所指向的对象'ABC'")
print("b=", b)
a = 'XYZ'
print("a='XYZ' 4.创建了对象'XYZ', a变量指向它")
print("a=", a)
print("这时的b变量还是指向的是对象'ABC', b=", b)

