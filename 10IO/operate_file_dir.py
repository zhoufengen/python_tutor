#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
Python内置的os模块也可以直接调用操作系统提供的接口函数。
""")

import os
print("操作系统类型:", os.name)
print("当前目录:", os.getcwd())
print("当前目录的文件:", os.listdir('.'))

print("""
环境变量：
os.environ
要获取某个环境变量的值，可以调用os.environ.get('key')：
""")
print("HOME=", os.environ.get("HOME"))


print("""
操作文件和目录：
""")
print("查看当前目录的绝对路径:", os.path.abspath('.'))
print("创建一个目录之前先拼装路径:", os.path.join('.', 'testdir'))
#print("创建目录：", os.mkdir('./testdir'))
#print("删除目录：", os.rmdir('./testdir'))

print("""
把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数;
要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数;
os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便;
对文件重命名;os.rename('test.txt', 'test2.py')
删掉文件;os.remove('test2.py')

但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。
幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。

""")

print("拆分出目录和文件名：", os.path.split('/Users/michael/testdir/file.txt'))
print("获取文件扩展名：", os.path.splitext('/Users/michael/testdir/file.txt'))

#print("对文件重命名：", os.rename('test.txt', 'test.ini'))
#print("删除文件：", os.remove('test.ini'))


print("列出当初目录下的所有文件和文件夹：")
for i in os.listdir('.'):
    print(i)



print("编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径:")

def find_file(path, filename):
    for i in os.listdir(path):
        if os.path.isfile(os.path.join(path, i)): #判断是否是文件: 拼装出来的路径+文件名
            if filename in i:  #包含指定字符串的文件
                print(os.path.join(path, i))
        else:
            find_file(os.path.join(path, i), filename)



find_file('.', 'test2')

print("""
常见错误：直接使用os.listdir()的返回值当做os.path.isdir()和os.path.isfile()的入参
正确用法：需要先使用python路径拼接os.path.join()函数，将os.listdir()返回的名称拼接成文件或目录的绝对路径再传入os.path.isdir()和os.path.isfile().

""")