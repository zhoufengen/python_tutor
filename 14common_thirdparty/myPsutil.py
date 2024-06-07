#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
用Python来编写脚本简化日常的运维工作是Python的一个重要用途。
在Linux下，有许多系统命令可以让我们时刻监控系统运行的状态，如ps，top，free等等。
要获取这些系统信息，Python可以通过subprocess模块调用并获取结果。但这样做显得很麻烦，尤其是要写很多解析代码。

在Python中获取系统信息的另一个好办法是使用psutil这个第三方模块。
psutil = process and system utilities，它不仅可以通过一两行代码实现系统监控，还可以跨平台使用，支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块。

安装psutil
如果安装了Anaconda，psutil就已经可用了。否则，需要在命令行下通过pip安装：
$ pip install psutil

获取CPU信息:
""")

import psutil
print("# CPU逻辑数量=", psutil.cpu_count())
print("# CPU物理核心=", psutil.cpu_count(logical=False))
print("# 4说明是4核超线程, 8则是8核非超线程")

print("统计CPU的用户／系统／空闲时间：", psutil.cpu_times())

print("再实现类似top命令的CPU使用率，每秒刷新一次，累计10次：(8个CPU的使用百分比)")
for x in range(1):
    print(psutil.cpu_percent(interval=1, percpu=True))


print("""
获取内存信息
使用psutil获取物理内存和交换内存信息，分别使用：
""")
print("物理内存：psutil.virtual_memory()=",  psutil.virtual_memory())
print("交换内存：psutil.swap_memory()=",  psutil.swap_memory())


print("""
获取磁盘信息
可以通过psutil获取磁盘分区、磁盘使用率和磁盘IO信息：
""")
print("磁盘分区信息:", psutil.disk_partitions())
print("磁盘使用率:", psutil.disk_usage('/'))
print("磁盘IO:", psutil.disk_io_counters())

print("""
获取网络信息
psutil可以获取网络接口和网络连接信息：
""")

print("获取网络读写字节／包的个数:", psutil.net_io_counters())
print("获取网络接口信息:", psutil.net_if_addrs())
print("获取网络接口状态:", psutil.net_if_stats())
#print("获取TCP连接信息:", psutil.net_connections())   #sudo python myPsutil.py

print("""
获取进程信息
通过psutil可以获取到所有进程的详细信息：
""")

print("psutil.pids()=", psutil.pids())
p = psutil.Process(113)
print("获取指定进程ID=113 psutil.Process(113)=", psutil.Process(113))
print("获取进程名:", p.name())
print("获取进程路径:", p.exe())
#print("获取进程命令行参数:", p.cmdline())
#print("获取进程的工作目录:", p.cwd())
print("获取进程的父进程ID:", p.ppid())
print("获取进程的父进程:", p.parent())
print("获取进程的子进程:", p.children())
print("获取进程的状态:", p.status())
print("获取进程的用户名:", p.username())
print("获取进程的启动时间:", p.create_time())
print("获取进程的终端:", p.terminal())
print("进程使用的CPU时间:", p.cpu_times())
print("进程打开的文件:", p.open_files())
print("进程使用的内存:", p.memory_info())
print("进程相关网络连接:", p.connections())
print("进程的线程数量:", p.num_threads())
print("所有线程的信息:", p.threads())
print("进程环境变量:", p.environ())
print("结束进程:", p.terminate())

print("""
psutil还提供了一个test()函数，可以模拟出ps命令的效果：
psutil.test()
""")



