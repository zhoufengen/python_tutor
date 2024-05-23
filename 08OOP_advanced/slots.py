#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging

logging.basicConfig(level=logging.DEBUG)

print("""
__slots__ 限制实例只能绑定某些属性：
""")

class Student(object):
    pass

jack = Student()
jack.name = 'Jack'
print(jack.name)
jack.age = 25
print(jack.age)

class Student(object):
    __slots__ = ('name', 'age', 'set_age')


bob = Student()
bob.name = 'Bob'
print(bob.name)
bob.age = 25
print(bob.age)

try:
    print("绑定一个不在__slots__中定义的属性，bob.score = 99 结果会报错:")
    bob.score = 99
    print(bob.score)
except AttributeError as e:
    logging.exception("Caught Exception: %s", e)


print("""
也可以限制绑定方法：
""")

def set_age(self, age):
    print("这是一个用来绑定的方法：")
    self.age = age

from types import MethodType
print("给bob实例绑定一个方法：bob.set_age = MethodType(set_age, bob)：")
bob.set_age = MethodType(set_age, bob)
bob.set_age(25)
print(bob.age)

print("一旦用了__slots__限制。如果尝试给实例绑定一个不在它其中的属性，就会报错：")

print("""
刚刚给一个实例bob绑定属性和方法，其他的实例是没这个属性的，所以报错：
要想所有的实例都有绑定的属性和方法，可以给类绑定：
""")

Student.set_age = MethodType(set_age, Student)

michel = Student()
michel.set_age(25)
print(michel.age)

lisa = Student()
lisa.set_age(35)
print(lisa.age)


print("""
__slots__定义的属性只在当前类中生效，如果是子类不会继承：
如果子类定义了__slots__属性，那子类的限制就是子类的__slots__加上父类的__slots__：
""")

class Student2(object):
    __slots__ = ('name', 'age')

class GraduateStudent(Student2):
    __slots__ = ('score')


try:
    print("子类GraduateStudent的__slots__属性是score，所以子类实例不能绑定score属性：")
    g = GraduateStudent()
    g.score = 99
    g.name = 'Madison'
    g.age = 25
    print(g.score)
    print(g.name)
    print(g.age)

    g.gender = 'F'
    print(g.gender)
except AttributeError as e:
    logging.exception("Caught Exception: %s", e)

