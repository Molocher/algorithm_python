#!/usr/bin/env python
# _*_ coding=utf-8 _*_

'''
@author:moloqu
@file:sum.py
@time:2020/5/30 15:02
'''


def sum(arr):
    if len(arr) == 0:
        return 0
    else:
        head = arr[0]
        arr.pop(0)
        result = head + sum(arr)
        return result


def count(arr):
    if len(arr) == 0:
        return 0
    else:
        arr.pop(0)
        return (1 + count(arr))


if __name__ == '__main__':
    print(sum([1,2,3,4]))
    print(count([1,2,3,4,5]))
    # arr = [1,2,3,4]
    # print(arr.pop(0))
    # print(arr)