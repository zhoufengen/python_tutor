#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.DEBUG)

print("""
使用特殊函数定制类：
特殊的函数如下：
__slots__
__len__
__str__
__repr__
__iter__
__getitem__
__getattr__
__call__
__next__
""")

class Foo(object):
   __slots__ = ('name',)
   __len__ = lambda self: 10

   def __init__(self, name):
       self.name = name

   def __str__(self):
       return 'Foo(name=%s)' % self.name

   __repr__ = __str__



foo = Foo('foo')
foo.name = 'Michel'
print("限制动态绑定属性：name=", foo.name)
print("foo可以作用于len函数：len=", len(foo))
print("foo可以作用于str函数：foo=", foo)

print("__iter__使Fib类的实例可以迭代：")

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a


    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L




fib = Fib()
for n in fib:
    print(n)


print("__getitem__使Fib类的实例可以下标访问：")
print("fib[5]=", fib[5])

print("__getitem__使Fib类的实例可以切片访问：")
print("fib[5:10]=", fib[5:10])


print("__getattr__实例调用没有定义的属性时，定制返回相应的值：")
class Student(object):
    def __init__(self):
        self.name = 'Michel'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


myStudent = Student()
print("myStudent.score=", myStudent.score)

try:
    print("myStudent.age=", myStudent.age)
except AttributeError as e:
    logging.exception("Caught Exception：%s", e)


print("__getattr__也可以定制返回一个函数：")
print("myStudent.age=", myStudent.age())

print("""
这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。
现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：
http://api.server/user/friends
http://api.server/user/timeline/list
还有些REST API会把参数放到URL中，比如GitHub的API：
http://github/users/123/repos
""")

print("写一个类，返回的是请求的url：")
class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        if path == 'users':
            return lambda userId: Chain('%s/%s' % (self._path, userId))
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


chain = Chain()
print("url1=", chain.api.service.user.friends)
print("url2=", chain.api.user.timeline.list)
print("url3=", chain.github.users(123).repos)

print("""
__call__使一个实例可以直接调用：
用callable()判断实例是否可以调用
""")

class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('__call__ My name is %s.' % self.name)


s1 = Student('Michel')
print(f"callable(s1)={callable(s1)}, s1()={s1()}")