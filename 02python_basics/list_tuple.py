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


myList.append(123)
myList.append(True)
myList.append('Dinosaur')
print("list里面的元素的数据类型也可以不同=", myList)  


myList.insert(6, ['Apple', 'Orange'])
print("list元素也可以是另一个list", myList)
print("取出另一个list的元素=", myList[6][0], myList[6][1])  

emptyList = []
print("list可以一个元素都没有,此时list的len为0", "length=", len(emptyList))                  

print("++++++++++++++++++++++tuple+++++++++++++++++++++")
print("""另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改;
因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple;
tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来;
""")

myTuple = (1, 2, 3)
print("myTuple=", myTuple)

myTuple = (1, )
print("只有1个元素的tuple定义时必须加一个逗号,，来消除歧义=", myTuple)

print("tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！")
