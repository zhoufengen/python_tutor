#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。
在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念。
所以，面向对象的设计思想是抽象出Class，根据Class创建Instance。
面向对象的抽象程度又比函数要高，因为一个Class既包含数据，又包含操作数据的方法。
数据封装、继承和多态是面向对象的三大特点，我们后面会详细讲解。

""")


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


if __name__ == '__main__':
    bart = Student('Bart Simpson', 59)
    lisa = Student('Lisa Simpson', 87)
    bart.print_score()
    lisa.print_score()
