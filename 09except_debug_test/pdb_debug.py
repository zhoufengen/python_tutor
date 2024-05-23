#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)

print("""
这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点：
执行命令：
python pdb_debug.py

""")