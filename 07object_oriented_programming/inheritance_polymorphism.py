#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
继承有什么好处？最大的好处是子类获得了父类的全部功能。
继承的另一个好处：多态。
当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()

著名的“开闭”原则：
对扩展开放：允许新增Animal子类；
对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。


""")


class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')




def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())


print("""
静态语言 vs 动态语言
对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
""")

class Timer(object):
    def run(self):
        print('Start...')

run_twice(Timer())




