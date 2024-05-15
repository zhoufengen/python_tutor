#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print("""
if ... elif ... elif ... else ...判断时，会写很长一串代码，可读性较差
match case 语句除了可以匹配简单的单个值外，还可以匹配多个值、匹配一定范围，并且把匹配后的值绑定到变量
可以在最后（且仅能在最后）加一个case _表示“任意值”
""")

score = 'B'

match score:
  case 'A':
    print("score is A!")
  case 'B':
    print("score is B!")
  case 'C':
    print("score is C!")
  case _:
    print("score is unknwon!")


print("""
match语句除了可以匹配简单的单个值外，还可以匹配多个值、匹配一定范围，并且把匹配后的值绑定到变量：
""")

age = 9

match age:
  case x if x < 10:
    print(f"< 10 years old: {x}")
  case 10:
    print("10 years old")
  case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
    print("11~18 years old")
  case 19:
    print("19 years old")
  case _:
    print(f"age is other that is not in 10~19!")

print("""
match语句还可以匹配列表，功能非常强大
""")

args = ["gcc", "hello.c", "world.c", "zhoufe"]
#args = ["gcc", "hello.c"]

match args:
  case ["gcc"]:
    print("one arg has been match")
  case ["gcc", file1, *files]:
    print("gcc 命令后面至少指定了一个文件,多个也可以:")
    print("gcc compile:" + file1 + "," + ",".join(files))
  case ["clean"]:
    print("clean")
  case _:
    print("invalid command!")
