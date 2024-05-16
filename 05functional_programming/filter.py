#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
filter的作用：
和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

""")

print("用埃式筛法筛选素数：")
print("构造奇数序列：是一个生成器：")
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

print("构造一个不能整除的筛选函数：返回的是函数f(x)")
def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列


print("打印1000以内的素数：")
for n in primes():
    if n < 1000:
        print(n)
    else:
        break

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print("筛选出素数：(有2个正因素，1和它本身的整除的数就叫素数：)")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(list(filter(is_prime, L)))

print("""
回数是指从左向右读和从右向左读都是一样的数：
""")

def is_palindrome(n):
    str_n = str(n)
    return str_n == str_n[::-1]

print("list(filter(is_palindrome, range(1, 200)))=", list(filter(is_palindrome, range(1, 200))))

output = filter(is_palindrome, range(1, 1000))
print('1~1000中含有的回数:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
