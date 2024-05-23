#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
需要一整套调试程序的手段来修复bug:
debug的手段：

1.用print()把可能有问题的变量打印出来看看
2.凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：
3.把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，
4.pdb 
   进入调试模式：
   python -m pdb err.py 
   
5.pdb.set_trace()
   在文件里写入：pdb.set_trace()打上断点
   执行到文件：
   python err.py 
   到该断点了才进入调试模式
   
6.IDE
   如果要比较爽地设置断点、单步执行，就需要一个支持调试功能的IDE。目前比较好的Python IDE有：
   Visual Studio Code：https://code.visualstudio.com/，需要安装Python插件。
   PyCharm：http://www.jetbrains.com/pycharm/
    
    另外，Eclipse加上pydev插件也可以调试Python程序。

""")

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


# foo('0')

import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)

print("""
python -m pdb err.py
以参数-m pdb启动后，pdb定位到下一步要执行的代码-> s = '0'。输入命令l来查看代码：

(Pdb) l
  1     # err.py
  2  -> s = '0'
  3     n = int(s)
  4     print(10 / n)
输入命令n可以单步执行代码：

任何时候都可以输入命令p 变量名来查看变量：

Pdb) p s
'0'
(Pdb) p n
0

输入命令q结束调试，退出程序：
(Pdb) q


""")