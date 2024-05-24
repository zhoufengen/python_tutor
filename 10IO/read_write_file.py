#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
读文件：
f = open('/Users/michael/test.txt', 'r')
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
标示符'r'表示读
'rb'模式表示二进制读

如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：
调用read(size)方法，每次最多读取size个字节的内容。


""")
with open('./test.txt', 'r') as f:
    while True:
        #line = f.read(1024)
        #line = f.readline()
        line = f.read()
        if len(line) == 0:
            break
        print(line)



print("""
写文件：
f = open('/Users/michael/test.txt', 'w')
'w'或者'wb'表示写文本文件或写二进制文件
可以传入'a'以追加（append）模式写入

你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。
只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险：


""")

with open('./test2.txt', 'w') as f:
    f.write("Hello world ! Write File")



fpath = './test.txt'

timezoneStr = ''
with open(fpath, 'r') as f:
    s = f.read()
    timezoneStr += s

print(timezoneStr)
