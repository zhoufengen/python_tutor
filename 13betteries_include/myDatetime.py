#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
datetime是Python处理日期和时间的标准库。

获取当前日期和时间:
""")
from datetime import datetime
print(datetime.now())

print("""
注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。
如果仅导入import datetime，则必须引用全名datetime.datetime。
datetime.now()返回当前日期和时间，其类型是datetime。

获取指定日期和时间:
""")
dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
print(dt)

print("""
datetime转换为timestamp

在计算机中，时间实际上是用数字表示的。
我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），
当前时间就是相对于epoch time的秒数，称为timestamp。

timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
对应的北京时间是：
timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00

可见timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了，
转换到任意时区的时间也是完全确定的，
这就是为什么计算机存储的当前时间是以timestamp表示的，
因为全球各地的计算机在任意时刻的timestamp都是完全相同的（假定时间已校准）。

把一个datetime类型转换为timestamp只需要简单调用timestamp()方法：
""")
dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
print(dt.timestamp())

print("""
注意Python的timestamp是一个浮点数，整数位表示 秒。
某些编程语言（如Java和JavaScript）的timestamp使用整数表示 毫秒 数，这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。

timestamp转换为datetime:
要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法：
""")
t = 1429417200.0
print(datetime.fromtimestamp(t)) #时间戳 转为本地的时区的datetime对象

print("""
注意到timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。
上述转换是在timestamp和本地时间做转换。
本地时间是指当前操作系统设定的时区。例如北京时区是东8区，则本地时间：
2015-04-19 12:20:00
实际上就是UTC+8:00时区的时间：
2015-04-19 12:20:00 UTC+8:00

而此刻的格林威治标准时间与北京时间差了8小时，也就是UTC+0:00时区的时间应该是：
2015-04-19 04:20:00 UTC+0:00

timestamp也可以直接被转换到UTC标准时区的时间：
""")
t = 1429417200.0
print("t = 1429417200.0 转为本地时区的datetime=", datetime.fromtimestamp(t))       #本地时间
print("t = 1429417200.0 转为UTC标准时区的datetime=", datetime.utcfromtimestamp(t)) # UTC时间

print("""
str转换为datetime:
把str转换为datetime。转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串：
""")
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print("datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')=", cday, "cday.tzinfo", cday.tzinfo)

print("""
字符串'%Y-%m-%d %H:%M:%S'规定了日期和时间部分的格式。
注意转换后的datetime是没有时区信息的。
""")

print("""
datetime转换为str:
需要转换为str，转换方法是通过strftime()实现的，同样需要一个日期和时间的格式化字符串：
""")
now = datetime.now()
print("now.strftime('%a, %d %b %Y %H:%M:%S %z')=", now.strftime('%a, %d %b %Y %H:%M:%S %z'))
print("now.strftime('%Y-%m-%d %H:%M:%S')=", now.strftime('%Y-%m-%d %H:%M:%S'))

print("""
datetime加减:
对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类：
""")

from datetime import datetime, timedelta
now = datetime.strptime("2024-05-30 15:09:01", "%Y-%m-%d %H:%M:%S")
print("now=", now)
print("now + 1 day=", now + timedelta(days=1))
print("now + 1 week=", now + timedelta(weeks=1))
print("now - 1 day=", now - timedelta(days=1))
print("now - 1 week=", now - timedelta(weeks=1))
print("now + 1 hour=", now + timedelta(hours=1))
print("now - 1 hour=", now - timedelta(hours=1))
print("""
timedelta对象表示的时间段，可以进行加减，也可以进行比较。
""")

dt1 = datetime.strptime("2024-05-30 15:09:01", "%Y-%m-%d %H:%M:%S")
dt2 = datetime.strptime("2024-05-31 15:09:01", "%Y-%m-%d %H:%M:%S")
print("dt1=", dt1)
print("dt2=", dt2)
#比较dt1 和 dt2
print("dt1 < dt2=", dt1 < dt2)
print("dt1 > dt2=", dt1 > dt2)
print("dt1 == dt2=", dt1 == dt2)
print("dt1 - dt2=", dt1 - dt2)
#print("dt1 + dt2=", dt1 + dt2) 不支持加法

print("""
本地时间转换为UTC时间
本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。（标准时间是UTC+0:00时区的时间）

一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区：
""")
from datetime import datetime, timedelta, timezone
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
dt = datetime.strptime("2015-6-1 18:19:59", "%Y-%m-%d %H:%M:%S")
dt = dt.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
print("dt=", dt, "dt.tzinfo=", dt.tzinfo)

print("""
如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区。
""")
#tz_utc_7 = timezone(timedelta(hours=7)) # 创建时区UTC+8:00
#dt = datetime.strptime("2015-6-1 18:19:59", "%Y-%m-%d %H:%M:%S")
#dt = dt.replace(tzinfo=tz_utc_7) # 强制设置为UTC+7:00
#print("dt=", dt, "dt.tzinfo=", dt.tzinfo)

print("""
时区转换
我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间：
""")
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print("utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc) 拿到UTC时间，并强制设置时区为UTC+0:00=", utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print("utc_dt.astimezone(timezone(timedelta(hours=8))) astimezone()将转换时区为北京时间=", bj_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print("utc_dt.astimezone(timezone(timedelta(hours=9))) astimezone()将转换时区为东京时间=", tokyo_dt)

print("bj_dt.astimezone(timezone(timedelta(hours=9))) 北京时间直接转东京时间，不用先转UTC时间=", bj_dt.astimezone(timezone(timedelta(hours=9))))


print("""
假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：
""")

import re

dt_str = '2015-1-21 9:01:30'
time_format = '%Y-%m-%d %H:%M:%S'
tz_str = 'UTC+5:00'

def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, time_format)
    # 获取时区信息 利用正则表达式切分字符串
    str_tz = re.split(r'[UTC:]+', tz_str)[1]
    print(str_tz)
    tz = timezone(timedelta(hours=int(str_tz)))
    dt = dt.replace(tzinfo=tz)
    return (dt - datetime(1970, 1, 1, tzinfo=timezone.utc)).total_seconds()

print("to_timestamp(dt_str, tz_str)=", to_timestamp(dt_str, tz_str))


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
print("t1=", t1)
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
print("t2=", t2)
assert t2 == 1433121030.0, t2

print('ok')