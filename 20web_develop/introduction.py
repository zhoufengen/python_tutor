#!/usr/bin/python3
# -*- coding: utf-8 -*-
print("""
Client/Server模式简称CS架构。
Browser/Server模式开始流行，简称BS架构。
CS架构不适合Web，最大的原因是Web应用程序的修改和升级非常迅速，而CS架构需要每个客户端逐个升级桌面App，
在BS架构下，客户端只需要浏览器，应用程序的逻辑和数据都存储在服务器端。浏览器只需要请求服务器，获取Web页面，并把Web页面展示给用户即可。
今天，除了重量级的软件如Office，Photoshop等，大部分软件都以Web形式提供。比如，新浪提供的新闻、博客、微博等服务，均是Web应用。

Web应用开发可以说是目前软件开发中最重要的部分。Web开发也经历了好几个阶段：
1.静态Web页面：

2.动态Web页面：
要处理用户发送的动态数据，出现了Common Gateway Interface，简称CGI，用C/C++编写。

3.ASP/JSP/PHP：与HTML结合紧密，因此，迅速取代了CGI模式

4.MVC：为了解决直接用脚本语言嵌入HTML导致的可维护性差的问题，Web应用也引入了Model-View-Controller的模式，来简化Web开发。

5.目前，Web开发技术仍在快速发展中，异步开发、新的MVVM前端技术层出不穷。


HTTP协议：
每个HTTP请求和响应都遵循相同的格式，一个HTTP包含Header和Body两部分，其中Body是可选的。
HTTP协议是一种文本协议，所以，它的格式也非常简单。

HTTP GET请求的格式：

GET /path HTTP/1.1
Header1: Value1
Header2: Value2
Header3: Value3

每个Header一行一个，换行符是\r\n。

HTTP POST请求的格式：

POST /path HTTP/1.1
Header1: Value1
Header2: Value2
Header3: Value3

body data goes here...

当遇到连续两个\r\n时，Header部分结束，后面的数据全部是Body。

HTTP响应的格式：

200 OK
Header1: Value1
Header2: Value2
Header3: Value3

body data goes here...

HTTP响应如果包含body，也是通过\r\n\r\n来分隔的。
请再次注意，Body的数据类型由Content-Type头来确定，如果是网页，Body就是文本，如果是图片，Body就是图片的二进制数据。
当存在Content-Encoding时，Body数据是被压缩的，最常见的压缩方式是gzip，
所以，看到Content-Encoding: gzip时，需要将Body数据先解压缩，才能得到真正的数据。压缩的目的在于减少Body的大小，加快网络传输。


HTML：

网页就是HTML？这么理解大概没错。
我们来看看最简单的HTML长什么样：
<html>
<head>
  <title>Hello</title>
</head>
<body>
  <h1>Hello, world!</h1>
</body>
</html>

CSS简介：
CSS是Cascading Style Sheets（层叠样式表）的简称，CSS用来控制HTML里的所有元素如何展现。

<html>
<head>
  <title>Hello</title>
  <style>
    h1 {
      color: #333333;
      font-size: 48px;
      text-shadow: 3px 3px 3px #666666;
    }
  </style>
</head>
<body>
  <h1>Hello, world!</h1>
</body>
</html>

JavaScript简介：
JavaScript虽然名称有个Java，但它和Java真的一点关系没有。
JavaScript是为了让HTML具有交互性、有动作。

<html>
<head>
  <title>Hello</title>
  <style>
    h1 {
      color: #333333;
      font-size: 48px;
      text-shadow: 3px 3px 3px #666666;
    }
  </style>
  <script>
    function change() {
      document.getElementsByTagName('h1')[0].style.color = '#ff0000';
    }
  </script>
</head>
<body>
  <h1 onclick="change()">Hello, world!</h1>
</body>
</html>

WSGI:
我们用Python专注于生成HTML文档。因为我们不希望接触到TCP连接、HTTP原始请求和响应格式，
所以，需要一个统一的接口，让我们专心用Python编写Web业务。
这个接口就是WSGI：Web Server Gateway Interface。

复杂的Web应用程序，光靠一个WSGI函数来处理还是太底层了，
我们需要在WSGI之上再抽象出Web框架，进一步简化Web开发。



flask:
直接选择一个比较流行的Web框架——Flask来使用。
$ pip install flask

//app.py
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()

$ python app.py 
 * Running on http://127.0.0.1:5000/
 
 
除了Flask，常见的Python Web框架还有：

Django：全能型Web框架；
web.py：一个小巧的Web框架；
Bottle：和Flask类似的Web框架；
Tornado：Facebook的开源异步Web框架。 


web模板：jinja2
Web框架把我们从WSGI中拯救出来了。现在，我们只需要不断地编写函数，带上URL，就可以继续Web App的开发了。
但是，Web App不仅仅是处理逻辑，展示给用户的页面也非常重要。
Flask通过render_template()函数来实现模板的渲染。
和Web框架类似，Python的模板也有很多种。Flask默认支持的模板是jinja2，所以我们先直接安装jinja2：
$ pip install jinja2

用来显示登录表单的模板：
<html>
<head>
  <title>Please Sign In</title>
</head>
<body>
  {% if message %}
  <p style="color:red">{{ message }}</p>
  {% endif %}
  <form action="/signin" method="post">
    <legend>Please sign in:</legend>
    <p><input name="username" placeholder="Username" value="{{ username }}"></p>
    <p><input name="password" placeholder="Password" type="password"></p>
    <p><button type="submit">Sign In</button></p>
  </form>
</body>
</html>

除了Jinja2，常见的模板还有：

Mako：用<% ... %>和${xxx}的一个模板；
Cheetah：也是用<% ... %>和${xxx}的一个模板；
Django：Django是一站式框架，内置一个用{% ... %}和{{ xxx }}的模板。


""")