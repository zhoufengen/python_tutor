#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
在Python中，一个.py文件就称之为一个模块（Module）。
Python又引入了按目录来组织模块的方法，称为包（Package）。
每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。
__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是目录名称。
例如包目录：mycompany 下面有 __init__.py: 模块名：mycompany，对应的文件是__init__.py

""")