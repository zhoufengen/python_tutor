#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import time

from flask import Flask, jsonify, request, make_response

app = Flask(__name__)


class R(object):
    def __init__(self, code=0, data={}, message='', success=True):
        self.code = code
        self.data = data
        self.message = message
        self.success = success

    @staticmethod
    def ok():
        r = R()
        r.code = 200
        r.data = {}
        r.message = 'success'
        r.success = True
        return r

    @staticmethod
    def fail():
        r = R()
        r.code = 500
        r.data = {}
        r.message = 'fail'
        r.success = False
        return r

    #json序列化
    def to_dict(self):
        return {
            'code': self.code,
            'data': self.data,
            'message': self.message,
            'success': self.success
        }


@app.route('/getUserInfo', methods=['GET'])
def getUserInfo():
    r = R.ok()
    r.data = {'name': 'zfe', 'age': 18}
    print("request.headers=", request.headers, type(request.headers))
    print("request.headers['User-Agent']=", request.headers['User-Agent'])
    print("request.headers['Accept-Encoding']=", request.headers['Accept-Encoding'])
    return jsonify(r.to_dict())



@app.route('/getUserInfoII', methods=['GET'])
def getUserInfoII():
    params_data = request.args
    print("请求的路径上拼接的（？号&号拼接的）参数：params_data=", params_data, type(params_data))
    r = R.ok()
    r.data = {'name': 'zfe2', 'zfe': 200}
    return jsonify(r.to_dict())

@app.route('/postUserInfo', methods=['POST'])
def postUserInfo():
    post_data = request.get_json()
    print("post_data=", post_data, type(post_data))
    post_data['age'] = 19
    r = R.ok()
    r.data = post_data
    return jsonify(r.to_dict())



@app.route('/postUserInfoII', methods=['POST'])
def postUserInfoII():
    form_data = request.data
    print("post_data=", form_data, type(form_data))
    r = R.ok()
    r.data = {'name': 'zfe3', 'age': 13}
    return jsonify(r.to_dict())


@app.route('/postFiles', methods=['POST'])
def postFiles():
    files = request.files.getlist('file')
    print("files=", files, type(files))
    for file in files:
        print("file=", file, type(file))
    r = R.ok()
    r.data = {'name': 'zfe4', 'age': 14}
    return jsonify(r.to_dict())


@app.route('/getResponseHeaders', methods=['GET'])
def getResponseHeaders():
    r = R.ok()
    r.data = {'name': 'zfe4response', 'age': 14}
    return jsonify(r.to_dict()), 200, {'X-UUID': 'xxx-xxx-1'}  #设置请求头：{'X-UUID': 'xxx-xxx-1'}


@app.route('/getCookies', methods=['GET'])
def getCookies():
    print("request.cookies=", request.cookies, type(request.cookies))
    print("request.cookies['name']=", request.cookies['name'])
    print("request.cookies['age']=", request.cookies['age'])
    r = R.ok()
    r.data = {'name': 'zfe4cookie', 'age': 14}

    resp = make_response(jsonify(r.to_dict()))  #返回的数据
    resp.set_cookie("name", "python")           #设置cookie
    resp.set_cookie("age", "go")

    return resp


@app.route('/getTimeout', methods=['GET'])
def getTimeout():
    r = R.ok()
    r.data = {'name': 'zfe4timeout', 'age': 14}
    time.sleep(3)
    return jsonify(r.to_dict())






if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8125)
