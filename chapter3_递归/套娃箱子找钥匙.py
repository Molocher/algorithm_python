#!/usr/bin/env python
# _*_ coding=utf-8 _*_

'''
@author:moloqu
@file:套娃箱子找钥匙.py
@time:2020/5/30 11:29
'''


# 伪代码
def look_for_key_while(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print("found the key")


def look_for_key_digui(box):
    for item in box:
        if item.is_a_box():
            look_for_key_digui(item)
        elif item.is_a_key():
            print("found the key")
