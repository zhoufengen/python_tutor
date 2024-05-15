#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = list(range(100))
print(L)
print("取前10个元素：")
print("L[:10]=", L[:10])

print("取后10个元素：")
print("L[-10:]=", L[-10:])

print("从1的位置开始取到11位置的元素10个元素：")
print("L[1:11]=", L[1:11])

print("全list，每隔2-1=1个元素取一个元素")
print("L[::2]=", L[::2])

print("从索引1开始，到索引11-1=10，每隔3-1=2个元素取一个元素")
print("L[1:11:3]=", L[1:11:3])

print("从索引1开始，到索引11-1=10，每隔3-1=2个元素取一个元素，取倒序")
print("L[1:11:3][::-1]=", L[1:11:3][::-1])

print("从索引0开始，到索引11-1=10，取到了11-0=11个元素：")
print(L[0:11])
print("从索引1开始，到索引11-1=10，取到11-10=10个元素：")
print(L[1:11])


print("利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：")

def my_trim(s):
    if s == '':
        return ''
    elif s[0] == ' ':
        return my_trim(s[1:])
    elif s[-1] == ' ':
        return my_trim(s[:-1])
    else:
        return s


print("trim('   ABC  ')=", my_trim('   ABC  '))


# 测试:
if my_trim('hello  ') != 'hello':
    print('测试失败!')
elif my_trim('  hello') != 'hello':
    print('测试失败!')
elif my_trim('  hello  ') != 'hello':
    print('测试失败!')
elif my_trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif my_trim('') != '':
    print('测试失败!')
elif my_trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')





