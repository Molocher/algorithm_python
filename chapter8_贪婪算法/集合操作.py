# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 17:10
# @Author  : Molo.Qu


fruits = set(['avocado','tomato','banana'])
vegetables = set(['beets','carrots','tomato'])
print(fruits | vegetables)#并集
print(fruits & vegetables)#交集
print(fruits - vegetables)#差集