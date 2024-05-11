#!/usr/bin/env python3
# -*- coding: utf-8 -*-
sum = 0
for x in [1, 2,3,4,5,6,7,8,9,10]:
  sum += x
print("sum=", sum)

for x in ['Dog', 'Cat', 'Cow']:
   print("x=", x)


print("Python提供一个range()函数，可以生成一个0~100的整数序列，再通过list()函数可以转换为list")
sum = 0
for i in list(range(101)):
   sum += i

print("sum=", sum)

oddNum = 0
evenNum = 0
n = 100
while True:
  if n % 2 != 0:
    oddNum += n
  else:
    evenNum += n
  n = n - 1
  if n <= 0:
    break

print("oddNum=", oddNum, "evenNum=", evenNum)

n = 0
while n < 10:
  n = n + 1
  if n % 2 == 0:
     continue
  print("odd=", n)

