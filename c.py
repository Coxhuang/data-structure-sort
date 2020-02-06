# -*- coding: utf-8 -*-
"""
@Time ： 2020/2/6 13:37
@Auth ： Minhang
@File ：c.py
@IDE  ：PyCharm
"""

def f(x,l=[]):
    for i in range(x):
        l.append(i)

    print(l)

f(2) # [0, 1] - [0, 1]
f(3,[3,2,1]) # [3,2,1,0,1,2]
f(3) # [0, 1, 2]

# a = {
#     "A":1,
#     "B":2,
#     "C":3
# }
#
# b = max(a.values())
# print(b)
#
# c = max(a.items(),key=lambda x:x[1])
# print(c)
#
# list_10 = [foo/2 for foo in range(0,8,1) ]
# print(list_10)
#
# import numpy as np
#
# def my_avg(*args):
#     np.mean(args)
#
#
# def func(*args,**kwargs):
#
#     print(args)
#     print(kwargs)
#
# func(1,1,2)
#
#
# class MyCls(object):
#
#     @staticmethod
#     def func():
#
#         print("func")
#
# MyCls.func()