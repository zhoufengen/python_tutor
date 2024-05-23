#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

print("""
在代码运行期间动态增加功能的方式，称之为“装饰器”
本质上，decorator就是一个返回函数的高阶函数。
我们要定义一个能打印日志的decorator，可以定义如下：
""")

def log(func):
    def wrapper(*args, **kw):
        print('log call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

print("借助Python的@语法，把decorator置于函数的定义处:")


print("调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志:")
@log
def now():
    print('2015-3-25')


print("""
由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
""")
now()

print("如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：")
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('log call %s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')

print("和两层嵌套的decorator相比，3层嵌套的效果是这样的：now = log('execute')(now)")
nowVar = log('execute')(now)
nowVar()

print("看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：")
print("nowVar.__name__=", nowVar.__name__)

print("""那就需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：
""")
import functools



def log1(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('log11 call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

import functools


def log1(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('log12 call %s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log1('execute')
def now():
    print('2015-3-25')

wrapper = log1('execute')(now)
wrapper()

print("看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：")
print("wrapper.__name__=", wrapper.__name__)

print("now()= %s, now function name is=%s" % (now(), now.__name__))

print("""
请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间:
""")


import time

#自己写的
def performance(text):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kw):
            t1 = time.time()
            result = fn(*args, **kw)
            t2 = time.time()
            print('%s call %s() in %s ms' % (text, fn.__name__, (t2 - t1) * 1000))
            return result
        return wrapper
    return decorator

def timing_decorator(message):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()  # 记录函数开始执行的时间
            result = func(*args, **kwargs)  # 执行函数
            end_time = time.time()  # 记录函数结束执行的时间
            print(f"{message}: {func.__name__} executed in {end_time - start_time:.4f} seconds")  # 打印带有自定义消息的执行时间
            return result
        return wrapper
    return decorator


@timing_decorator('exec1')
def fun1(name, age):
    time.sleep(10)

@timing_decorator('exec2')
def fun2(name, age, score):
    time.sleep(15)

@timing_decorator('exec3')
def fun3():
    time.sleep(20)


# print("fun1()", fun1("zhangsan1", 20))
# print("fun2()", fun2("zhangsan2", 20, 100))
# print("fun3()", fun3())




# 测试
@timing_decorator('fast')
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@performance('slow1111')
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

else:
    print('测试成功!')








