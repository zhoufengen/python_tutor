#!/usr/bin/env python3
# -*- coding: utf-8 -*-


print("""
MySQL官方提供了mysql-connector-python驱动，但是安装的时候需要给pip命令加上参数--allow-external：
$ pip install mysql-connector-python --allow-external mysql-connector-python

如果上面的命令安装失败，可以试试另一个驱动：
$ pip install mysql-connector
""")

# 导入MySQL驱动:
import mysql.connector
# 注意把password设为你的root口令:
conn = mysql.connector.connect(host='10.132.136.3', port='8000', user='root', password='VtYMVdfYz85RmwgfPcGhsg==', database='test')
cursor = conn.cursor()
# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
print('cursor.rowcount=', cursor.rowcount)
# 提交事务:
conn.commit()
cursor.close()
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print('values=', values)
# 关闭Cursor和Connection:
cursor.close()
conn.close()