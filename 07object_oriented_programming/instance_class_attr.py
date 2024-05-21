#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
实例属性: 通过实例访问的
类属性：通过类名访问的

给实例绑定属性的方法是通过实例变量，或者通过self变量
""")

class Student(object):
    name = 'Student'         #类属性的定义

    def __init__(self):
        self.name = 100      #实例属性的定义

    def __init__(self, name):
        self.name = name      #实例属性的定义


myStudent = Student('bob')
print("myStudent.name=", myStudent.name)
print("Student.name=", Student.name)

myStudent.name = 'Michael'
print("myStudent.name=", myStudent.name)
print("Student.name=", Student.name)

print("删除实例属性的值：")
del myStudent.name
print("myStudent20.name=", myStudent.name)

print("""
""")
class Student2(object):
    name = 'Student2'


myStudent20 = Student2()
myStudent21 = Student2()
print("myStudent20.name=", myStudent20.name)
print("myStudent21.name=", myStudent21.name)
print("Student2.name=", Student2.name)

myStudent20.name = 'Michael'
print("给实例属性赋值myStudent20.name = 'Michael'，myStudent20.name=", myStudent20.name)
print("myStudent21.name=", myStudent21.name)
print("Student2.name=", Student2.name)

print("删除实例属性的值：")
del myStudent20.name
print("del myStudent20.name 删除了实例属性的值，myStudent20.name会恢复为类属性的值：=", myStudent20.name)

print("""
实例属性优先于类属性：
实例属性的定义可以和类属性和并起来，也可以单独写在__init__中；
实例属性赋值时会覆盖类属性的值；
如果删除该实例属性的值，则它会变为类属性的值；
""")


print("""
为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
""")
class Student3(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student3.count += 1


# 测试:
if Student3.count != 0:
    print('测试失败!')
else:
    bart = Student3('Bart')
    if Student3.count != 1:
        print('测试失败!')
    else:
        lisa = Student3('Lisa')
        if Student3.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student3.count)
            print('测试通过!')