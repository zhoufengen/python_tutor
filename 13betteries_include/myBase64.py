#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
Base64是一种用64个字符来表示任意二进制数据的方法。
Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。

Base64的原理很简单:
首先，准备一个包含64个字符的数组：
['A', 'B', 'C', ... 'a', 'b', 'c', ... '0', '1', ... '+', '/']
然后，对二进制数据进行处理，每3个字节一组，一个字节8bit，一共是3x8=24bit，再划为4组，每组正好6个bit：一组一个数字，
这样我们得到4个数字作为索引，然后查表（刚刚准备的64个字符的数组），获得相应的4个字符，这就是编码后的字符串。
所以，Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%，好处是编码后的文本数据可以在邮件正文、网页等直接显示。

如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，
表示补了多少字节（补一个=号就是补了1个字节，补两个=号就是补了2个字节），解码的时候，会自动去掉。
Python内置的base64可以直接进行base64的编解码：
""")
import base64

print("base64.b64encode(b'binary\x00string')=", base64.b64encode(b'binary\x00string'))
decode = base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
print("base64.b64decode(b'YmluYXJ5AHN0cmluZw==')=", decode)
# 二进制转字符串
print("str(decode)=", str(decode))
print("decode.decode('ascii')=", decode.decode('ascii'))

print("""
由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
""")

print("base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')=", base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print("base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')=", base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print("base64.urlsafe_b64decode('abcd--__')=", base64.urlsafe_b64decode('abcd--__'))

print(r"""
Python对bytes类型的数据用带b前缀的单引号或双引号表示：
x = b'ABC'
要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：
>>> 'ABC'.encode('ascii')
b'ABC'
#>>> '中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'
#>>> '中文'.encode('ascii')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。
在bytes中，无法显示为ASCII字符的字节，用\x##显示。
反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
#>>> b'ABC'.decode('ascii')
'ABC'
#>>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
'中文'
如果bytes中包含无法解码的字节，decode()方法会报错：
#>>> b'\xe4\xb8\xad\xff'.decode('utf-8')
Traceback (most recent call last):
#  ...
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 3: invalid start byte""")

bVar = b'ABC'
print("type(bVar)=", type(bVar))

print(r"""
Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等。
由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉：
# 标准Base64:
'abcd' -> 'YWJjZA=='
# 自动去掉=:
'abcd' -> 'YWJjZA'
""")
print("base64.b64encode(b'abcd')=", base64.b64encode(b'abcd'))
#print("base64.b64decode(b'abcd').decode('ascii')=", base64.b64decode(b'abcd').decode('ascii'))

print("""
去掉=后怎么解码呢？因为Base64是把3个字节变为4个字节，所以，Base64编码的长度永远是4的倍数，因此，需要加上=把Base64字符串的长度变为4的倍数，就可以正常解码了。
请写一个能处理去掉=的base64解码函数：
""")
import base64

def safe_base64_decode(s):
    if len(s) % 4 == 0:
        return base64.b64decode(s)
    else:
        return base64.b64decode(s + '=' * (4 - len(s) % 4))

# 测试:
assert b'abcd' == safe_base64_decode('YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode('YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')




