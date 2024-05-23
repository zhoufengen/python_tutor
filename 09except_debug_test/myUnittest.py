#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
这种以测试为驱动的开发模式最大的好处就是:
确保一个程序模块的行为符合我们设计的测试用例。
在将来修改的时候，可以极大程度地保证该模块行为仍然是正确的。
""")

print("""我们来编写一个Dict类，这个类的行为和dict一致，但是可以通过属性来访问，用起来就像下面这样：
>>> d = Dict(a=1, b=2)
>>> d['a']
1
>>> d.a
1
""")

class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)


    def __setattr__(self, key, value):
        self[key] = value

print("""
运行单元测试
一旦编写好单元测试，我们就可以运行单元测试。最简单的运行方式是在mydict_test.py的最后加上两行代码：

if __name__ == '__main__':
    unittest.main()

这样就可以把mydict_test.py当做正常的python脚本运行：
$ python mydict_test.py

另一种方法是在命令行通过参数-m unittest直接运行单元测试：
python -m unittest mydict_test
这是推荐的做法，因为这样可以一次批量运行很多单元测试，并且，有很多工具可以自动来运行这些单元测试。


setUp与tearDown
可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。



""")


if __name__ == '__main__':
    d = Dict(a=1, b=2)
    print("d['a']=", d['a'], "d.a=", d.a)


