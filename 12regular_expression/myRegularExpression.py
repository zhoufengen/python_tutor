#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""

###############基础###############
字符串是编程时涉及到的最多的一种数据结构，对字符串进行操作的需求几乎无处不在。
比如   判断   一个字符串是否是合法的Email地址，虽然可以编程   提取    @前后的子串，再分别判断是否是单词和域名，但这样做不但麻烦，而且代码难以复用。

正则表达式是一种用来匹配字符串的强有力的武器。它的设计思想是用一种描述性的语言来给字符串定义一个规则，凡是符合规则的字符串，我们就认为它“匹配”了，否则，该字符串就是不合法的。

所以我们判断一个字符串是否是合法的Email的方法是：
1.创建一个匹配Email的正则表达式；
2.用该正则表达式去匹配用户的输入来判断是否合法。

因为正则表达式也是用字符串表示的，所以，我们要首先了解如何用字符来描述字符。
在正则表达式中，如果直接给出字符，就是精确匹配。

定长字符串：
用\d可以匹配一个数字，\w可以匹配一个字母或数字，所以：
'00\d'可以匹配'007'，但无法匹配'00A'；
'\d\d\d'可以匹配'010'；
'\w\w\d'可以匹配'py3'；
\s可以匹配一个空格（也包括Tab等空白符）；

.可以匹配任意一个字符，所以：
'py.'可以匹配'pyc'、'pyo'、'py!'等等。

变长字符串：
用*表示任意个字符（包括0个或者1到多个）
用+表示至少一个字符
用?表示0个或1个字符
用{n}表示n个字符
用{n,m}表示n-m个字符：

来看一个复杂的例子：\d{3}\s+\d{3,8}。
\d{3}表示匹配3个数字，例如'010'；
\s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格，例如匹配' '，' '等；
\d{3,8}表示3-8个数字，例如'1234567'。
综合起来，上面的正则表达式可以匹配以任意个空格隔开的带区号的电话号码。
如：123 12345678
如果要匹配'010-12345'这样的号码呢？由于'-'是特殊字符，在正则表达式中，要用'\'转义，所以，上面的正则是\d{3}\-\d{3,8}。
但是，仍然无法匹配'010 - 12345'，因为带有空格。所以我们需要更复杂的匹配方式。
###############基础###############
###############进阶###############
要做更精确地匹配，可以用[]表示一个字符的范围，比如：
[0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；
[0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；
[a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；
[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。
A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。()作用是分组。
^表示行的开头，^\d表示必须以数字开头。
$表示行的结束，\d$表示必须以数字结束。
你可能注意到了，py也可以匹配'python'，但是加上^py$就变成了整行匹配，就只能匹配'py'了。
###############进阶###############

""")

import re
matchBool = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
print("开头3个数字，中间-，结尾3到8个数字，匹配结果：010-12345=", matchBool)
matchBool = re.match(r'^\d{3}\-\d{3,8}$', '010 12345')
print("开头3个数字，中间-，结尾3到8个数字，匹配结果：010 12345=", matchBool)

test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')


print("""
切分字符串
用正则表达式切分字符串比用固定的字符更灵活，请看正常的切分代码：
'a b   c'.split(' ')
['a', 'b', '', '', 'c']

嗯，无法识别连续的空格，用正则表达式试试：
re.split(r'\s+', 'a b   c')
['a', 'b', 'c']

无论多少个空格都可以正常分割。加入,试试：
re.split(r'[\s\,]+', 'a,b, c  d')
['a', 'b', 'c', 'd']

re.split(r'[\s\,\;]+', 'a,b;; c  d')
['a', 'b', 'c', 'd']
如果用户输入了一组标签，下次记得用正则表达式来把不规范的输入转化成正确的数组。
""")

print("""
分组
除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）。比如：
""")

print("^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码：")
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print("m.group(0)=", m.group(0))
print("m.group(1)=", m.group(1))
print("m.group(2)=", m.group(2))

print("""
如果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来。
注意到group(0)永远是与整个正则表达式相匹配的字符串，group(1)、group(2)……表示第1、2、……个子串。

提取子串非常有用。来看一个更凶残的例子：
>>> t = '19:05:30'
>>> m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
>>> m.groups()
('19', '05', '30')

""")

print("""
贪婪匹配
最后需要特别指出的是，正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。举例如下，匹配出数字后面的0：
""")
groups = re.match(r'^(\d+)(0*)$', '102300').groups()
print("re.match(r'^(\d+)(0*)$', '102300').groups()=", groups)
print("""
由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配不出来，加个?就可以让\d+采用非贪婪匹配：
""")
print("re.match(r'^(\d+?)(0*)$', '102300').groups()=", re.match(r'^(\d+?)(0*)$', '102300').groups())

print("""
编译
当我们在Python中使用正则表达式时，re模块内部会干两件事情：
1.编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
2.用编译后的正则表达式去匹配字符串。
如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：
""")

import re
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print("re_telephone.match('010-12345').groups()=", re_telephone.match('010-12345').groups())
print("re_telephone.match('010-8086').groups()=", re_telephone.match('010-8086').groups())


print("""
编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串。
""")

print("""
请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
someone@gmail.com
bill.gates@microsoft.com
bill.ga1tes@microsoft.com
bill.ga1tes.zhou@microsoft.com
bill.ga1tes.zhou@microsoft.com.cn
""")
reg = re.compile(r'^(\w+(\.*\w*)*)@((\w+)(\.\w+)*)$')
print("reg.match('someone@gmail.com'),groups()=", reg.match('someone@gmail.com').groups())
print("reg.match('bill.gates@microsoft.com').groups()=", reg.match('bill.gates@microsoft.com').groups())
print("reg.match('bill.gat1es@microsoft.com').groups()=", reg.match('bill.gat1es@microsoft.com').groups())
print("reg.match('bill.gat1es.zhou@microsoft.com').groups()=", reg.match('bill.gat1es.zhou@microsoft.com').groups())
match = reg.match('bill.gat1es.zhou@microsoft.co1m.cn')
print("reg.match('bill.gat1es.zhou@microsoft.com.cn').groups()=", match.groups())






