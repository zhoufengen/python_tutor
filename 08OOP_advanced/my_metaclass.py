#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。

h = Hello()
type()函数：
可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，
而h是一个实例，它的类型就是class Hello。
""")

class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

h = Hello()
print("h.hello()=", h.hello())
print("type(Hello)=", type(Hello))
print("type(h)=", type(h))


print("""
我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。
type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：
""")

def fn(self, name='world2'): # 先定义函数
    print('Hello, %s.' % name)

Hello2 = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
h2 = Hello2()
print("h2.hello()=", h2.hello('111'))
print("type(Hello2)=", type(Hello2))
print("type(h2)=", type(h2))

print("""
要创建一个class对象，type()函数依次传入3个参数：
1.class的名称；
2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
""")


print("""
除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
metaclass，直译为元类，简单的解释就是：
当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
""")

print("""
在Python中，metaclass（元类）是一种特殊类型的类，它定义了类的创建方式。类是对象的模板，而元类就是类的模板。在Python中，一切皆对象，类本身也是一个对象，而且是一个特殊的对象。元类负责构造和修改类，它控制类的创建过程。
理解元类可以通过以下几个关键点来加深理解：
1.类的创建：在Python中，类是由type这个元类创建的。当你定义一个类时，Python会使用type来创建这个类的实例。
2.type函数：type不仅仅是一个函数，它还是一个元类。你可以使用type来创建新的类或者修改现有的类。
3.类的属性和方法：类具有属性和方法，元类也有自己的属性和方法。类的属性和方法存储在__dict__中，而元类的属性和方法存储在__class__中。
4.继承元类：类可以继承自其他类，同样，元类也可以继承自其他元类。通过继承type或自定义元类，可以改变类的创建方式。
5.自定义元类：通过继承type，可以创建自定义的元类来控制类的创建过程。自定义元类可以修改类的行为，比如修改类的属性、添加新的方法、改变类的初始化过程等。
__new__和__init__方法：在类的创建过程中，type会调用__new__方法来创建类的实例，然后调用__init__方法来初始化这个实例。在自定义元类中，可以通过重写这些方法来改变类的创建和初始化过程。
6.使用场景：元类通常用于框架和库的开发中，用于提供一种机制来自动注册类、检查类的结构、修改类的定义等。例如，数据库的ORM（对象关系映射）框架可能会使用元类来自动为数据库表生成对应的类。
""")

print("""我们先看一个简单的例子，这个metaclass可以给我们自定义的MyList增加一个add方法：
定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：
# metaclass是类的模板，所以必须从`type`类型派生：
""")
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


print("""有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass：""")
class MyList(list, metaclass=ListMetaclass):
    pass

print("""
当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。
__new__()方法接收到的参数依次是：
当前准备创建的类的对象；
1.类的名字；
2.类继承的父类集合；
3.类的方法集合。
""")

L = MyList()
L.add(1)
print("L=", L)

print("""
而普通的list没有add()方法：
动态修改有什么意义？直接在MyList定义中写上add()方法不是更简单吗？正常情况下，确实应该直接写，通过metaclass修改纯属变态。
但是，总会遇到需要通过metaclass修改类定义的。ORM就是一个典型的例子。

""")








