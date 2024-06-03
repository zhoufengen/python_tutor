#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#利用urllib读取JSON，然后将JSON解析为Python对象：
import urllib.request, urllib.parse, urllib.error
import json


def fetch_data(url):
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    jsObj = json.loads(data)
    print("jsObj=", jsObj, type(jsObj))
    return jsObj




# 测试
URL ='http://127.0.0.1:8824/get'
data = fetch_data(URL)
print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')

