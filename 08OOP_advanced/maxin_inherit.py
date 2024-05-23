#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from socketserver import TCPServer, ForkingMixIn, UDPServer, ThreadingMixIn

print("""
MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。
""")

class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass


class RunnableMixIn(object):
    def run(self):
        print('Running...')


class FlyableMixIn(object):
    def fly(self):
        print('Flying...')


class Dog(Mammal, RunnableMixIn):
    pass


class Bat(Mammal, FlyableMixIn):
    pass


print("""
Python自带的很多库也使用了MixIn。
举个例子，Python自带了TCPServer和UDPServer这两类网络服务，
而要同时服务多个用户就必须使用多进程或多线程模型，这两种模型由ForkingMixIn和ThreadingMixIn提供。通过组合，我们就可以创造出合适的服务来。
""")


class MyTcpServer(TCPServer, ForkingMixIn):
    pass

class MyUdpServer(UDPServer, ThreadingMixIn):
    pass

print("如果你打算搞一个更先进的协程模型，可以编写一个CoroutineMixIn：")
class CoroutineMixIn(object):
    def handle(self):
        self.request.send(b'Hello, world!')


class MyTCPServer(TCPServer, CoroutineMixIn):
    pass



