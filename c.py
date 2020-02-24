# -*- coding: utf-8 -*-
"""
@Time ： 2020/2/6 13:37
@Auth ： Minhang
@File ：c.py
@IDE  ：PyCharm
"""

# def f(x,l=[]):
#     for i in range(x):
#         l.append(i)
#
#     print(l)
#
# f(2) # [0, 1] - [0, 1]
# f(3,[3,2,1]) # [3,2,1,0,1,2]
# f(3) # [0, 1, 2]

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
#
# a = [1,2,3,4,5,6]
# print(a)
# b = len(a)
# for index in range(b):
#     print(index)
#     # a.pop(0)

# print(" love ".join(["Everyday","Yourself","Python",]))

# L1 =['abc', ['123','456']]
# L2 = ['1','2','3']
# print(L1 > L2)
# def func(a,*b):
#     for item in b:
#         a += item
#     return a
# m = 0
# print(func(m,1,1,2,3,5,7,12,21,33))
#
# a = ["a","b","c"]
# b = a[::-1]
# print(b)
#
#
# print(1.3 - 1.0 == 0.3)
# def c(test=""):
#     print(test)
#     def a(func):
#         def b(*args, **kw):
#             print("装饰器")
#             print(kw)
#             print(args)
#             return func(*args, **kw)
#         return b
#     return a
#
# @c("kkkk")
# def xxx(x,y):
#     print("主函数")
#     return None
#
# xxx(x=1,y=2)

#
# for foo in range(10,-1,-2):
#     print(foo)
# print("------")
for foo in range(4):
    print(foo)
    break
else:
    print("000")





