#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import ChainMap
import os, argparse

# 构造缺省参数:
defaults = {
    'color': 'red',
    'user': 'guest'
}

# 构造命令行参数:
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = { k: v for k, v in vars(namespace).items() if v }

# 组合成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])

#没有任何参数时，打印出默认参数：
#$ python myChainMap.py
#color=red
#user=guest

#当传入命令行参数时，优先使用命令行参数：
#$ python myChainMap.py -u bob
#color=red
#user=bob

#同时传入命令行参数和环境变量，命令行参数的优先级较高：
#$ user=admin color=green python myChainMap.py -u bob
#color=green
#user=bob

