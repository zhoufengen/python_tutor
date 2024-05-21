#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，
比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。

定义类是通过class关键字：
class Student(object):
    pass
    

紧接着是(object)，表示该类是从哪个类继承下来的，
通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。

创建出Student的实例，创建实例是通过类名+()实现的:
bart = Student()

在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
 注意：特殊方法“__init__”前后分别有两个下划线！！！
 
 在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：
 
 
 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。
 除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。
 
 既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在Student类的内部定义访问数据的函数，
 这样，就把“数据”给封装起来了。这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法：
 class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))
        
        
封装的另一个好处是可以给Student类增加新的方法，比如get_grade：

class Student(object):
    ...

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


        



 

""")