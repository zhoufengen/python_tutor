#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket

print("""
我们来看看如何通过UDP协议传输数据。和TCP类似，使用UDP的通信双方也分为客户端和服务器。服务器首先需要绑定端口：
""")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s.bind(('127.0.0.1', 9129))
print("""
创建Socket时，SOCK_DGRAM指定了这个Socket的类型是UDP。绑定端口和TCP一样，但是不需要调用listen()方法，而是直接接收来自任何客户端的数据：
recvfrom()方法返回数据和客户端的地址与端口，这样，服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端。
""")
print('Bind UDP on 9129...')
while True:
    # 接收来自客户端的数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    # 发送数据回客户端
    s.sendto(b'Hello, %s!' % data, addr)



