#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('select * from user where id=?', ('1',))
users = cursor.fetchall()
print('users=', users)
cursor.close()
conn.close()