#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
""")

import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

print("""
如果子进程还需要输入，则可以通过communicate()方法输入：
""")
import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print("output:%s" % output.decode('utf-8'))
print('Exit code:', p.returncode)

