#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
由于关系数据库的多个表还可以用外键实现一对多、多对多等关联，相应地，ORM框架也可以提供两个对象之间的一对多、多对多等功能。
例如，如果一个User拥有多个Book，就可以定义一对多关系如下：
""")

# 导入:
from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


# 创建对象的基类:
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多:
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:VtYMVdfYz85RmwgfPcGhsg==@10.132.136.3:8000/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
print('user.book1.name:', user.books[0].name)
print('user.book2.name:', user.books[1].name)
# 关闭Session:
session.close()

