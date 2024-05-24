#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。
""")

print("""
StringIO:
""")


from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())


f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())



print("""
BytesIO:
""")

from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
read = f.read()
print(str(read, 'utf-8'))
#

