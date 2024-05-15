#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间。
在Python中，这种一边循环一边计算的机制，称为生成器：generator。
""")

print("generator的两种定义方法：")
print("第一种：列表生成式不用[]而是用():")
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
generator = (x * x for x in L)
print("generator=", generator)
for n in generator:
    print(n)

print("第二种：函数中使用yield:")

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

generator_fib = fib(10)
print("generator_fib=", generator_fib)
for n in generator_fib:
    print(n)


print(""""
这里，最难理解的就是generator函数和普通函数的执行流程不一样。
普通函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，
再次执行时从上次返回的yield语句处继续执行。请看：
""")

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

try:
    o = odd()
    print("next(o)=", next(o))
    print("next(o)=", next(o))
    print("next(o)=", next(o))
    print("next(o)=", next(o))
except Exception as e:
    print(e)


g = fib(10)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break




print("杨辉三角：把每一行看做一个list，试写一个generator，不断输出下一行的list：")
print("杨辉三角的写法：")
def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]

n = 0
results = []
for i in triangles():
    results.append(i)
    n = n + 1
    if n == 10:
        break

for i in results:
    print(i)

print("注意：[i for i in range(0)] range(0)是空，所以不会生成任何元素，该列表生成式不会生成列表。")

