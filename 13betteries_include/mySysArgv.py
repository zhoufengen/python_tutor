#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""在命令行程序中，经常需要获取命令行参数。Python内置的sys.argv保存了完整的参数列表，我们可以从中解析出需要的参数：
python mySysArgv.py source.txt copy.txt 
""")
import sys
print(sys.argv)
source = sys.argv[1]
target = sys.argv[2]
print('sys.argv=', type(sys.argv), 'source=', source, 'target=', target)


#$ mySysArgv.py source.txt copy.txt
