#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
我们已经讲解了Python内置的urllib模块，用于访问网络资源。但是，它用起来比较麻烦，而且，缺少很多实用的高级功能。
更好的方案是使用requests。它是一个Python第三方库，处理URL资源特别方便。

安装requests
如果安装了Anaconda，requests就已经可用了。否则，需要在命令行下通过pip安装：
$ pip install requests

使用requests
要通过GET访问一个页面，只需要几行代码：
""")

import requests

baseUrl = 'http://127.0.0.1:8125'
r = requests.get('%s/getUserInfo' % baseUrl) # 豆瓣首页
print("r.status_code=", r.status_code)
print("r.text=", r.text)

print("""
对于带参数的URL，传入一个dict作为params参数：
requests自动检测编码，可以使用encoding属性查看： r.encoding

""")

r = requests.get('%s/getUserInfoII' % baseUrl, params={'q': 'python', 'cat': '1001'})
print("查看实际请求的URL：r.url=", r.url, 'r.text=', r.text, 'r.encoding=', r.encoding)

print("无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象：r.content=", r.content)

print("requests的方便之处还在于，对于特定类型的响应，例如JSON，可以直接获取：r.json()=", r.json())


print("需要传入HTTP Header时，我们传入一个dict作为headers参数：")


r = requests.get('%s/getUserInfo' % baseUrl, headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit', 'X-UID': 'xxx-id'})
print("r.text=", r.text)

print("""
要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据：
""")
r = requests.post('%s/postUserInfoII' % baseUrl, data={'form_email': 'abc@example.com', 'form_password': '123456'})
print("r.text=", r.content)

print("""
requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数：
""")
r = requests.post('%s/postUserInfo' % baseUrl, json={'json': 'json data', 'json1': 'json1data'})
print("r.text=", r.text)

print("""
类似的，上传文件需要更复杂的编码格式，但是requests把它简化成files参数：
""")
upload_files = {'file': open('code.jpg', 'rb')}
r = requests.post('%s/postFiles' % baseUrl, files=upload_files)
print("r.text=", r.text)

print("""
在读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度。
把post()方法替换为put()，delete()等，就可以以PUT或DELETE方式请求资源。
除了能轻松获取响应内容外，requests对获取HTTP响应的其他信息也非常简单。例如，获取响应头：
""")

r = requests.get('%s/getResponseHeaders' % baseUrl)
print("r.text=", r.text)

print("""
requests对Cookie做了特殊处理，使得我们不必解析Cookie就可以轻松获取指定的Cookie：
""")

myCs = {'name': 'abc', 'age': '12'}
r = requests.get('%s/getCookies' % baseUrl, cookies=myCs)
print("r.text=", r.text)
print("r.cookies=", r.cookies)


print("""
最后，要指定超时，传入以秒为单位的timeout参数：
""")

r = requests.get('%s/getTimeout' % baseUrl, timeout=2.5)       #2.5秒超时
print("r.text=", r.text)



