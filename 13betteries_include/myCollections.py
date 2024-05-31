#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
collections是Python内建的一个集合模块，提供了许多有用的集合类。


namedtuple
namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
例如，一个点的二维坐标就可以表示成：
""")

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print("p.x=", p.x, "p.y=", p.y)

print("""
类似的，如果要用坐标和半径表示一个圆，也可以用namedtuple定义：
""")

Circle = namedtuple('Circle', ['x', 'y', 'r'])
cir = Circle(1, 2, 3)
print("cir.x=", cir.x, "cir.y=", cir.y, "cir.r=", cir.r)

print("""
deque
使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。

""")
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')   #从尾部
q.appendleft('y') #从左边（头部）
print("q=", q)

print("""
defaultdict
使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
""")
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print("dd['key1']=", dd['key1'])
print("dd['key2']=", dd['key2'])

print("""
OrderedDict
使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
如果要保持Key的顺序，可以用OrderedDict：
""")
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print("d=", d)
print("od=", od)

print("注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：")
ld = OrderedDict()
ld['z'] = 1
ld['y'] = 2
ld['x'] = 3
print("ld=", ld)
print("list(ld.keys())=", list(ld.keys()))

print("""
OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
""")
from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)



luod = LastUpdatedOrderedDict(3)
luod['x'] = 1
luod['y'] = 2
luod['z'] = 3
luod['u'] = 4
print("会把最早添加进来的x key给删除：luod=", luod)


print("""
ChainMap
ChainMap可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找。
举个例子：应用程序往往都需要传入参数，参数可以通过命令行传入，可以通过环境变量传入，还可以有默认参数。我们可以用ChainMap实现参数的优先级查找，即先查命令行参数，如果没有传入，再查环境变量，如果没有，就使用默认参数。
""")



print("""
Counter是一个简单的计数器，例如，统计字符出现的个数：
""")

from collections import Counter
c = Counter()
for ch in 'programming wweee':
    c[ch] = c[ch] + 1

print("c=", c)

c.update("hello")
print("c=", c)