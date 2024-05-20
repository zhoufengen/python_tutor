#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("一般来说，第三方库都会在Python官方的pypi.python.org网站注册.")
print("安装Pillow的命令就是：")
print("pip install Pillow")
print("""
安装常用模块:
推荐直接使用Anaconda，这是一个基于Python的数据处理和科学计算平台，
它已经内置了许多非常有用的第三方库，我们装上Anaconda，就相当于把数十个第三方模块自动安装好了，非常简单易用。
Anaconda会把系统Path中的python指向自己自带的Python，
并且，Anaconda安装的第三方模块会安装在Anaconda自己的路径下，不影响系统已安装的Python目录。
""")

print("""
模块搜索路径：
当我们试图加载一个模块时，Python会在指定的路径下搜索对应的.py文件，如果找不到，就会报错：
默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中：
""")
import sys
print(sys.path)

print("""
如果我们要添加自己的搜索目录，有两种方法：
一是直接修改sys.path，添加要搜索的目录：
""")
import sys
sys.path.append('/Users/michael/my_py_scripts')
print("python搜索模块的目录：")
for path in sys.path:
    print(path)
print("这种方法是在运行时修改，运行结束后失效。")
print("""
第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。
设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。
""")




