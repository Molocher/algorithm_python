#!/usr/bin/env python
# _*_ coding=utf-8 _*_

'''
@author:moloqu
@file:快速排序.py
@time:2020/5/30 15:59
'''

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)



if __name__ == '__main__':
    print(quicksort([10,5,2,3]))