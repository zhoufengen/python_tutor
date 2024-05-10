#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。")

myList = ['Dog', 'Cat', 'Bird']
print("myList=", myList)

print("取最后一个元素:myList[-1]=", myList[-1])

myList.append('Cow')
print("末尾追加:myList.append('Cow')=", myList)

myList.insert(1, 'People')
print("指定位置插入:myList.insert(1, 'People')=", myList)

lastElement = myList.pop()
print("删除末尾的元素myList.pop()=", lastElement)
print("myList=", myList)

index1Element = myList.pop(1)
print("删除指定的元素myList.pop(1)=", index1Element)
print("myList=", myList)                        
