#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from elasticsearch import Elasticsearch

from datetime import datetime

# Elasticsearch服务器的主机名和端口
es_host = "10.20.2.43"
es_port = 9200
# Elasticsearch的用户名和密码
es_username = "elastic"
es_password = "NRMIlNEszwqGDlw_cpt5"

# 创建Elasticsearch连接，包含HTTP基本认证

es = Elasticsearch(
    "https://elastic:NRMIlNEszwqGDlw_cpt5@10.20.2.43:9200",
    verify_certs=False,
    ca_certs=False
)



today0620 = datetime(2024, 6, 20, 12, 30, 0)
tomorrow0621 = datetime(2024, 6, 20, 12, 30, 0)

dt = tomorrow0621
# 生成长消息内容的函数
def generate_long_message():
    long_message = "这是一条很长的测试消息，用于填充Elasticsearch的message字段。" + dt.isoformat()
    return long_message * 100  # 重复100次以生成更长的内容
# 定义数据列表
data_list = [
    {
        "appName": "kcemanagement-auth",
        "timestamp": dt.isoformat(),
        "message": generate_long_message()
    }
    for _ in range(100)
]

# 写入数据到索引
def write_data_to_index(index_name, data):
    for item in data:
        try:
            res = es.index(index=index_name, document=item)
            print(f"Index: {index_name}, Result: {res.get('result')}")
        except Exception as e:
            print(f"Failed to index document: {e}")

# 索引名称
index_today0620 = "app-kcemanagerteam-kcemanagement-auth-dev-20240620"
index_tomorrow0621 = "app-kcemanagerteam-kcemanagement-auth-dev-20240621"

# 写入数据到今天的索引
#write_data_to_index(index_today0620, data_list)

# 写入数据到明天的索引
# 注意：这里假设今天是2024年6月20日，明天是2024年6月21日
# 如果今天是其他日期，你需要调整索引名称和timestamp
write_data_to_index(index_tomorrow0621, data_list)