#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：")
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print("f1()=", f1())
print("请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：")
print("f1==f2 ? ", f1 == f2)


print("""
闭包：
在Python中，闭包（Closure）是一个有趣的概念，它指的是那些能够访问自由变量的函数。
自由变量是指在函数中使用的，但既不是函数参数也不是函数内部定义的变量。
闭包通常由一个嵌套的函数组成，这个嵌套的函数能够记住并访问它外部作用域中的变量。
这使得闭包能够保持对这些外部变量的引用，即使外部函数已经执行完毕。
""")

def count(n):
    def increase(x):
        return n * x + 1
    return increase

increase = count(5)
print("count(5)=", increase(3))


print("返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。")
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print("f1=", f1(), "f2=", f2(), "f3=", f3())
print("都是9！！！")

print("如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：")
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count()
print("f1=", f1(), "f2=", f2(), "f3=", f3())

print("缺点是代码较长，可利用lambda函数缩短代码。")
def count():
    def f(i):
        return lambda : i*i
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count()
print("f1=", f1(), "f2=", f2(), "f3=", f3())

print("""
使用闭包，就是内层函数引用了外层函数的局部变量。如果只是读外层变量的值，我们会发现返回的闭包函数调用一切正常：
""")

def inc():
    x = 0
    def fn():
        # 仅读取x的值:
        return x + 1
    return fn

f = inc()
print(f()) # 1
print(f()) # 1

print("""
但是，如果对外层变量赋值，由于Python解释器会把x当作函数fn()的局部变量，它会报错：
使用闭包时，对外层变量赋值前，需要先使用nonlocal声明该变量不是当前函数的局部变量。
""")

def inc():
    x = 0
    def fn():
        nonlocal x
        # 写x的值:
        x = x + 1
        return x
    return fn

f1 = inc()
print("f1()=", f1(), f1())

print("利用闭包返回一个计数器函数，每次调用它返回递增整数：")
def createCounter():
    c = 0
    def counter():
        nonlocal c
        c = c + 1
        return c
    return counter


counter = createCounter()
print("createcCounter()=", counter())
print("createcCounter()=", counter())
print("createcCounter()=", counter())
print("createcCounter()=", counter())
print("createcCounter()=", counter())

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


