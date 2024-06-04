#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
HTML本质上是XML的子集，但是HTML的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML。
好在Python提供了HTMLParser来非常方便地解析HTML，只需简单几行代码：
""")
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('打印开始标签:<%s>' % tag)

    def handle_endtag(self, tag):
        print('打印结束标签:</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('打印开始结束标签:<%s/>' % tag)

    def handle_data(self, data):
        print("标签里的数据：", data)

    def handle_comment(self, data):
        print('打印评论：<!--', data, '-->')

    def handle_entityref(self, name):
        print('打印实体引用：&%s;' % name)

    def handle_charref(self, name):
        print('打印引用：&#%s;' % name)



parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')
