#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
Python提供了pickle模块来实现序列化。
""")



print("""
pickle:
""")
import pickle


d = dict(name='Bob', age=20, score=88)
print("pickle.dumps()方法把任意对象序列化成一个bytes:", pickle.dumps(d))
print("pickle.loads()方法反序列化出对象:", pickle.loads(pickle.dumps(d)))

print("把dict(name='Bob', age=20, score=88)对象序列号后写入一个文件:")
# with open('./dump.txt', 'wb') as f:
#     pickle.dump(d, f)

print("pickle.load()方法从一个文件中读取内容并反序列化:")
with open('./dump.txt', 'rb') as f:
    loadObj = pickle.load(f)
    print(loadObj)


print("""
Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。
""")

print("""
JSON:
""")


print("""
JSON和Python内置的数据类型对应如下：
JSON类型	     Python类型
{}	         dict
[]	         list
"string"	 str
1234.56	     int或float
true/false	 True/False
null	     None
""")


print("""
如何把Python对象变成一个JSON:
""")
import json
d = dict(name='Bob', age=20, score=88)
json_str = json.dumps(d)
print("json.dumps()方法把任意对象变成一个JSON格式的字符串:", json_str)
loadsObj = json.loads(json.dumps(d))
print("json.loads()方法把JSON的字符串变成一个Python对象:", loadsObj)
print("isinstance(loadsObj, dict)=:", isinstance(loadsObj, dict))

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def dict2Student(d):
        return Student(d['name'], d['age'], d['score'])

    # def __str__(self):
    #     return json.dumps(self, default=lambda obj: obj.__dict__)

s = Student('Bob', 20, 88)
studentStr = json.dumps(s, default=lambda obj: obj.__dict__)
print("json.dumps(s, default=lambda obj: obj.__dict__)方法把任意对象变成一个JSON格式的字符串:", studentStr)
studentObj = json.loads(studentStr, object_hook=Student.dict2Student)
print("json.loads(studentStr, object_hook=Student.dict2Student)方法把JSON的字符串变成一个Python对象:", studentObj)
print("isinstance(studentObj, Student)=:", isinstance(studentObj, Student))

print("""
对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响：
ensure_ascii=False 中文就不会转成unicode编码了。
""")

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
print(s)








