#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import traceback

print("编码: ASCII (不够用) -> GB2312(中国), Shift_JIS(日本), Euc-kr(韩国)  -> Unicode (统一) 节省空间 -> UTF-8")

print("包含中文的str: Python支持多语言!!!")

print("ord() 获取字符的整数表示:A=", ord('A'), "中=", ord('中'))

print("chr() 把编码转换为对应的字符:chr(65)=", chr(65), "chr(20013)=", chr(20013))

print(r"十六进制的Unicode编码: '\u4e2d\u6587'=", '\u4e2d\u6587')

print(r"十进制的Unicode编码: '\u20013\u25991'=", '\u20013\u25991')

print("在Python的内存中以Unicode表示, 字符串类型是str; 网络传输或者保存在磁盘上:就需要把str变为以字节为单位的bytes!!!")
print("Python对bytes类型的数据用带b前缀的单引号或双引号表")
x=b'ABC'
print("x=b'ABC'", x)

print('以Unicode表示的str通过encode()方法可以编码为指定的bytes')
x='ABC'.encode('ascii')
print('x=', x)


x='中文'.encode('utf-8')
print('x=', x)

try:
  x='中文'.encode('ascii')
  print('x=', x)
except Exception as e:
  stack_trace = traceback.format_exc()
  print(stack_trace)

print("从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法")

myDecode = b'ABC'.decode('ascii')
print(r"b'ABC'.decode('ascii')=", myDecode)

myDecode = b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print(r"b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')=", myDecode)

try:
  zw = b'\xe4\xb8\xad\xff'.decode('utf-8')
  print(r"b'\xe4\xb8\xad\xff'.decode('utf-8')=", zw)
except Exception as e:
  stack_trace = traceback.format_exc()
  print(stack_trace)

print("bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节")
zw = b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
print(r"b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')=", zw)


print("要计算str包含多少个字符，可以用len()函数")
mylen = len('ABC')
print("len('ABC')=", mylen)
mylen = len('中文')
print("len('中文')=", mylen)

print("换成bytes，len()函数就计算字节数")

print(r"len(b'ABC')=", len(b'ABC'))
print(r"len(b'\xe4\xb8\xad\xe6\x96\x87')=", len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(r"len('中文'.encode('utf-8'))=", len('中文'.encode('utf-8')))

print(r"格式化打印还是用f{s:.2f}种形式吧")

r=2.5
s = 3.14 * r ** 2

print(f"半径为{r}的圆的面积是{s:.3f}")
