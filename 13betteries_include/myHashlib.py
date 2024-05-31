#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。

MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit/16字节，通常用一个32位的16进制字符串表示。
SHA1的结果是160 bit/20字节，通常用一个40位的16进制字符串表示。
比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长。



什么是摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。
可见，摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。
""")

import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print("md5.hexdigest()=", md5.hexdigest())

print("如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：")
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print("md5.hexdigest()=", md5.hexdigest())



import hashlib

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print("sha1.hexdigest()=", sha1.hexdigest())

print("""
练习1：
根据用户输入的口令，计算出存储在数据库中的MD5口令：
""")
def calc_md5(password):
    m = hashlib.md5()
    m.update(password.encode('utf-8'))
    return m.hexdigest()

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    if db[user] == calc_md5(password):
        return True
    return False


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

print("""
练习2
根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：
""")
import hashlib, random

# db = {}
#
# def register(username, password):
#     db[username] = get_md5(password + username + 'the-Salt')

def get_md5(user, pws):
    m = hashlib.md5()
    m.update(user.salt.encode('utf-8'))
    m.update(pws.encode('utf-8'))
    return m.hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)]) # 生成随机的盐 防止同样的密码存储相同的MD5值
        print(username, "self.salt=", self.salt)
        self.password = get_md5(self, password)
        print(username, "self.password=", self.password)


db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}




def login(username, password):
    user = db[username]
    return user.password == get_md5(user, password)

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')


