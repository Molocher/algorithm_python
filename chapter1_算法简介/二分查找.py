# -*- coding: utf-8 -*-
# @Time    : 2020/5/29 10:36
# @Author  : Molo.Qu


# 二分查找是一种算法，其输入是一个有序的元素列表（必须有序的原因稍后解释）。如果要查找的元素包含在列表中，二分查找返回其位置；否则返回null。

# 对于包含n个元素的列表，用二分查找最多需要log₂n步


def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]  # 猜中间的数字
        if guess == item:  # 猜的数字命中
            return mid
        if guess > item:  # 猜的数字大了，最高位取中间位的前一位
            high = mid - 1
        else:
            low = mid + 1  # 猜的数字小了，最低位取中间位的上一位

    return None


if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 9]
    print(binary_search(my_list, 3))
    print(binary_search(my_list, -1))
