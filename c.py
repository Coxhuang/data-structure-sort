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

# def func(L):
#     queue = []
#     node = L
#
#     if node:
#         queue.append(node) # 根节点入队
#     else:
#         return None
#
#     while queue:
#         node = queue.pop(0) # 队首元素出队
#         if node.lchild: # 有左孩子
#             queue.append(node.lchild) # 左孩子入队
#         if node.rchild: # 有右孩子
#             queue.append(node.rchild) # 右孩子入队
#         print(node.data) # 打印出队元素数据


# a = [1]
# for foo in range(2, int(input())+1):
#     temp_list = [1]
#     for i in range(0,foo*2-2):
#         sum_node = 0
#         if len(a) > i and i >= 0:
#             sum_node += a[i]
#         if len(a) > i+1 and i+1 >= 0:
#             sum_node += a[i+1]
#         if len(a) > i-1 and i-1 >= 0:
#             sum_node += a[i-1]
#         temp_list.append(sum_node)
#     a = temp_list
# else:
#     for index, foo in enumerate(a):
#         if foo % 2 ==0:
#             break
#     else:
#         print(-1)
#     print(index+1)


# def fun(res, num):
#     if len(num) == 1: # 列表中油一个元素
#         if num[0] == res: # 列表元素等于res
#             return True
#         else:
#             return False
#     for i in range(len(num)):
#         a = num[i]
#         b = num[:] # 浅拷贝 num 列表
#         b.pop(i)
#         if (fun(res - a, b)) or fun(res * a, b) or fun(res / a, b) or fun(res + a, b):
#             return True
#
#
# while True:
#     try:
#         num = [int(i) for i in input().split()]
#         for i in range(4):
#             num[i] = float(num[i]) # 转成浮点型数据
#         if fun(24.0, num) == True:
#             print('true')
#         else:
#             print('false')
#     except:
#         break



# input_list = [1.0,2.0,3.0,4.0]
# # input_list = [1.0,2.0,10.0,2.0]
# c_list = ["+","-","*","/"]
# count = 0
# for x in c_list:
#     v1_list = input_list[:]
#     v1 = v1_list.pop(0)
#     for y in c_list:
#         v2_list = input_list[:]
#         v2 = v2_list.pop(1)
#         for z in c_list:
#             v3_list = input_list[:]
#             v3 = v3_list.pop(2)
#             v4 = v3_list.pop(2)
#             print(str(v1) + x + str(v2) + y + str(v3) + z + str(v4),"-----",eval(str(v1) + x + str(v2) + y + str(v3) + z + str(v4)))
#             count += 1


# a = [1.0,2.0,3.0,4.0]
a = [9.0,6.0,4.0,1.0]
b = ["+","-","*","/"]
count =0
for x in a:
    v1 = a[:]
    v1.remove(x)
    for y in v1:
        v2 = v1[:]
        v2.remove(y)
        for z in v2:
            v3 = v2[:]
            v3.remove(z)
            for x1 in b:
                for x2 in b:
                    for x3 in b:
                        print(str(x)+x1+str(y)+x2+str(z)+x3+str(v3[0]),"========",eval(str(x)+x1+str(y)+x2+str(z)+x3+str(v3[0])))
                        count +=1
print(count)

# def f(res,n):
#     x = False
#     if len(n) == 1:
#         if n[0] ==res:
#             print(n)
#             return True
#         else:
#             return False
#     for i in range(len(n)):
#         a = n[i]
#         b = n[:]
#         b.remove(a)
#         x = x or f(res-a,b) or f(res*a,b) or f(res/a,b) or f(res+a,b)
#     return x
# while True:
#     try:
#         n = input().split()
#         flag = False
#         if len(n) != 4:
#             print('false')
#             break
#         for i in range(4):
#             n[i] = float(n[i])
#         if f(24.0, n):
#             print('true')
#         else:
#             print('false')
#     except:
#         break





