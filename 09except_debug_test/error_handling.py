#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
所以高级语言通常都内置了一套try...except...finally...的错误处理机制，Python也不例外。
""")

try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

print("""
没错，可以有多个except来捕获不同类型的错误：
""")

try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')

print("""
此外，如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
""")

try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')


print("""
Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。比如：
""")

def foo():
    pass

try:
    foo()
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')


print("""
第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了。
""")

print("""
调用栈
我们从上往下可以看到整个错误的调用函数链：
出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。
""")

print("""
记录错误
Python内置的logging模块可以非常容易地记录错误信息：
通过配置，logging还可以把错误记录到日志文件里，方便事后排查。
""")


def bar(s):
    pass

import logging
logging.basicConfig(level=logging.DEBUG)
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


print("""
抛出错误
Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。
如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：
""")

class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n
try:
  foo('0')
except ValueError as e:
    print('ValueError!')


print("""
只有在必要的时候才定义我们自己的错误类型。如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），尽量使用Python内置的错误类型。
""")

print("""
最后，我们来看另一种错误处理的方式：向上抛异常：


""")

def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise
try:
  bar()
except Exception as e:
    print('Error!')

print("""
在bar()函数中，我们明明已经捕获了错误，但是，打印一个ValueError!后，又把错误通过raise语句抛出去了，这不有病么？
其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。
""")

print("""
raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：
try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')
""")


print("""
只要是合理的转换逻辑就可以，但是，决不应该把一个IOError转换成毫不相干的ValueError。
""")




from functools import reduce

def str2num(s):
    s = s.strip()
    #判断字符串为数字
    if s.isdigit():
        return int(s)
    elif s.replace('.', '', 1).isdigit():
        return float(s)
    raise ValueError(f'bad num {s}')
def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()

