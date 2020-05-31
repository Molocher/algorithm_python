#!/usr/bin/env python
# _*_ coding=utf-8 _*_

'''
@author:moloqu
@file:寻找芒果商.py
@time:2020/5/31 15:06
'''

from collections import deque

# 图
graph = {}
graph['you'] = ['alice', 'bob', 'claier']
graph['alice'] = ['peggy']
graph['bob'] = ['anuj', 'peggy']
graph['claier'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


def find():
    search_queue = deque()
    search_queue += graph['you']
    searched = []
    while search_queue:
        person = search_queue.popleft()  # 取出第一个人
        if person not in searched:
            if person_is_seller(person):  # 检查是否是芒果销售商
                print(person + 'is a mango seller!!!!')
                return True
            else:
                search_queue += graph[person]  # 不是芒果销售商，加入到搜索队列
                searched.append(person)

    return False


def person_is_seller(name):
    return name[-1] == 'm'

if __name__ == '__main__':
    print(find())
