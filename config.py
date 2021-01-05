# -- encoding: utf-8
# @time:         2021/1/3 下午12:44
# @Author:       hxy
# @Email:        976396706@qq.com
# @file:         config
# ----------------------------------
# 配好文件读取和写入
#
# ----------------------------------
import json


def read_conf(key):
    conf = load_file()
    value = conf.get(key)
    return value


def write_conf(key, value):
    conf = load_file()
    conf[key] = value
    file = json.dumps(conf)
    sava_file(file)


def load_file():
    with open('config.json', 'r') as f:
        conf = json.loads(f.read())
    return conf


def sava_file(file) -> object:
    with open('config.json', 'w') as f:
        f.write(file)
