#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from enum import Enum

print("""
枚举可以避免使用变量
""")
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print("Color.RED=%s Color.RED.value=%s" % (Color.RED, Color.RED.value))

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print("Month.Jan=", Month.Jan)

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


print("如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：")
class Weekday(Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 0

print(Weekday.Monday, Weekday.Monday.value, Weekday(1))