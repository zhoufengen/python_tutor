#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.DEBUG)

print("""
@property 
有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？对于追求完美的Python程序员来说，这是必须要做到的！
把一个属性变成get set方法，然后调用和赋值的时候就不需要调用方法，而是像属性访问那样直接.访问，或者=赋值；
""")

class Student(object):
    def __init__(self):
        self._score = 0
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError()

        self._score = value

s = Student()
s.score = 60
print(s.score)

class Student(object):
    def __init__(self):
        self._birth = 0
        self._age = 0
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2024 - self._birth


s1 = Student()
s1.birth = 2000
print(s1.birth)
print(s1.age)

print("""
还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：age就是不能set 值，所以会报错：
""")
try:
    s1.age = 11
except Exception as e:
    logging.exception("Caught Exception: %s", e)


print("""
要特别注意：属性的方法名不要和实例变量重名，会造成无限递归，最终导致栈溢出报错：
class Student(object):
    # 方法名称和实例变量均为birth:
    @property
    def birth(self):
        return self.birth #应该是：self._birth
""")