#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
在Python中，读写文件这样的资源要特别注意，必须在使用完毕后正确关闭它们。正确关闭文件资源的一个方法是使用try...finally：
""")

try:
    f = open('./myContextlib.py', 'r')
    f.read()
finally:
    if f:
        f.close()

print("""
写try...finally非常繁琐。Python的with语句允许我们非常方便地使用资源，而不必担心资源没有关闭，所以上面的代码可以简化为：
""")
with open('./myContextlib.py', 'r') as f:
    f.read()

print("""
实现上下文管理是通过__enter__和__exit__这两个方法实现的。例如，下面的class实现了这两个方法：
""")


class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)


print("这样我们就可以把自己写的资源对象用于with语句：")
with Query('Bob') as q:
    q.query()

print("""
编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法，上面的代码可以改写如下：
""")

from contextlib import contextmanager

class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')


print("""
@contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了：
""")

with create_query('Bob') as q:
    q.query()


print("""
很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现。例如：
""")


@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")


print("""
代码的执行顺序是：

1.with语句首先执行yield之前的语句，因此打印出<h1>；
2.yield调用会执行with语句内部的所有语句，因此打印出hello和world；
3.最后执行yield之后的语句，打印出</h1>。
因此，@contextmanager让我们通过编写generator来简化上下文管理。
""")


print("""
@closing
如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。例如，用with语句使用urlopen()：
""")

from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('http://www.baidu.com')) as page:
    for line in page:
        print(line)


print("""
closing也是一个经过@contextmanager装饰的generator，这个generator编写起来其实非常简单：
它的作用就是把任意对象变为上下文对象，并支持with语句。
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
@contextlib还有一些其他decorator，便于我们编写更简洁的代码。

""")







