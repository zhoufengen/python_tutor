#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
""")

myDict = {"Dog": 95, "Cat": 85, "Cow": 75}
for key in myDict:
    print("key=", key, "value=", myDict[key])

myDict['People'] = 45
print("给dict赋值myDict['People'] = 45:", myDict)
print("dict取值的两种方法1: myDict['Cow']=", myDict['Cow'])
print("[key]取值key如果不存在就会报错,方法2:myDict.get('Cow')=" , myDict.get('Cow'))
print("判断key存在dict中的方法:Bird' in myDict=", 'Bird' in myDict)
print("dict删除一对key-value的方法:myDict.pop('Cat')=", myDict.pop('Cat'))
print("myDict=", myDict)


print("正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象")


print("+++++++++++++++++++++++++++set++++++++++++++++++++")

print("set中的元素是不重复的, set传入的参数[1, 2, 3]是一个list")

mySet = set([1, 2, 3, 4])
print("mySet=", mySet)

print("mySet删除元素mySet.remove(4)=", mySet.remove(4))
print("mySet=", mySet)

aSet = set([1, 2, 3])
bSet = set([2, 3, 4])
print("set求交集 aSet={1, 2, 3}, bSet={2, 3, 4} 交集为=", aSet & bSet)
print("set求合集 aSet={1, 2, 3}, bSet={2, 3, 4} 合集为=", aSet | bSet)

