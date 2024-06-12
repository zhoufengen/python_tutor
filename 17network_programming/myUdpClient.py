#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket

print("""
客户端使用UDP时，首先仍然创建基于UDP的Socket，然后，不需要调用connect()，直接通过sendto()给服务器发数据：
""")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送给服务端的数据:
    print("给服务器（%s:%s）发送数据:" % ("127.0.0.1", 9129))
    s.sendto(data, ('127.0.0.1', 9129))
    # 接收来自服务端的数据:
    print(s.recv(1024).decode('utf-8'))
s.close()
