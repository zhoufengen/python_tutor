#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#用flask实现一个服务器，可以处理get请求和post请求并返回相应的json数据
from flask import Flask, request, jsonify

app = Flask(__name__)

# 处理GET请求的路由
@app.route('/get', methods=['GET'])
def handle_get():
    # 假设我们返回一些数据
    #assert data['query']['results']['channel']['location']['city'] == 'Beijing'
    data = {
        'message': 'This is a GET request',
        'data': [1, 2, 3, 4, 5],
        'query': {'results': {'channel': {'location': {'city': 'Beijing'}}}}
    }
    return jsonify(data)


# 处理POST请求的路由
@app.route('/post', methods=['POST'])
def handle_post():
    # 获取JSON数据
    json_data = request.get_json()
    if not json_data:
        return jsonify({'error': 'No JSON data provided'}), 400

    # 假设我们返回接收到的数据
    return jsonify({'message': 'This is a POST request', 'received_data': json_data})


if __name__ == '__main__':
    app.run(debug=True, port=8824)
