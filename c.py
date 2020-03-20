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
# a = [9.0,6.0,4.0,1.0]
# b = ["+","-","*","/"]
# count =0
# for x in a:
#     v1 = a[:]
#     v1.remove(x)
#     for y in v1:
#         v2 = v1[:]
#         v2.remove(y)
#         for z in v2:
#             v3 = v2[:]
#             v3.remove(z)
#             for x1 in b:
#                 for x2 in b:
#                     for x3 in b:
#                         print(str(x)+x1+str(y)+x2+str(z)+x3+str(v3[0]),"========",eval(str(x)+x1+str(y)+x2+str(z)+x3+str(v3[0])))
#                         count +=1
# print(count)

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

# import random
# n = 6
# out_list = []
# for x in range(1, n+1):
#     inner_list = []
#     for y in range(x):
#         inner_list.append(random.randint(1,9))
#     out_list.append(inner_list)
#
# print(out_list)
# for z in out_list:
#     print(z)
#
# out_list = [[6], [4, 5], [6, 3, 5], [6, 9, 5, 4], [8, 5, 9, 1, 4], [7, 6, 3, 7, 8, 8]]
# print(out_list)
# for index,z in enumerate(out_list):
#     p_str = ""
#     for c in range(6 - index):
#         p_str += " "
#     for i in z:
#         p_str += str(i) + " "
#     print(p_str)



# def func(x, y, f_list):
#
#     if x == 5: # 最底层
#         return f_list[x][y] # 返回最底层对应的某个元素
#     else:
#         return max(func(x+1,y,f_list),func(x+1,y+1,f_list)) + f_list[x][y]
#
#
# def haha():
#     out_list = [[3], [6, 6], [7, 10, 1], [10, 5, 7, 5], [8, 5, 4, 3, 4], [5, 4, 4, 7, 5, 5]]
#     n = len(out_list)
#     a = func(0,0,out_list)
#     print(a)
#
# haha()
#


# class Solution:
#     def maxValue(self, grid):
#
#         self.row = len(grid)  # 行数
#         self.col = len(grid[0])  # 列数
#
#         self.out_list = [] # 用于存储状态
#         for x in range(self.row):
#             inner_list = []
#             for y in range(self.col):
#                 inner_list.append(-1)
#             self.out_list.append(inner_list)
#
#         return self.dfs(0, 0, grid)
#
#
#     def dfs(self, x, y, grid):
#
#         if self.out_list[x][y] != -1:
#             ret = self.out_list[x][y]
#         elif y == self.col - 1 and x == self.row - 1:
#             ret = grid[x][y]
#         elif x >= (self.row - 1):
#             ret = self.dfs(x, y + 1, grid) + grid[x][y]
#         elif y >= (self.col - 1):
#             ret = self.dfs(x + 1, y, grid) + grid[x][y]
#         elif x < (self.row - 1) and y < (self.col - 1):
#             ret = max(self.dfs(x + 1, y, grid), self.dfs(x, y + 1, grid)) + grid[x][y]
#         else:
#             ret = 0
#             print("00000")
#         self.out_list[x][y] = ret
#         return ret
#
#
# Solution().maxValue([[1,3,1],[1,5,1],[4,2,1]])


# def func(a,b = ""):
#     b += "1"
#     print(a,b)
#
# func(a=2)
# func(2)
# func(2)


# x = 2
# def func():
#     global x
#     x = 1
#     return x
# func()
# print(x)  # 1


# str1 = "a12ahc"
# str2 = "c12ahf"
# record_list = [] # 记录公共子串位置的二维矩阵
# len_str = 0 # 最大子串长度
# stop = 0 # 最大子串末尾位置
#
# for x in str1: # 生成二维矩阵, 默认元素: 0
#     temp_list = []
#     for y in str2:
#         temp_list.append(0)
#     record_list.append(temp_list)
#
# for index_x, s1 in enumerate(str1): # 记录公共子串的位置
#     for index_y, s2 in enumerate(str2):
#         if s1 == s2:
#             if index_x == 0 or index_y == 0: # 当前元素位于上边界或者左边界
#                 record_list[index_x][index_y] = 1
#             else:
#                 record_list[index_x][index_y] = record_list[index_x-1][index_y-1] + 1 # 左上角加1
#
#         if record_list[index_x][index_y] > len_str:
#             stop = index_y # 记录最大子串位置
#             len_str = record_list[index_x][index_y] # 最大子串长度
#
# print(str1[stop-len_str+1:stop+1])
# ret_list = [] # 存放获取的公共子串
# for index_x, value_list in enumerate(record_list):
#     for index_y, v in enumerate(value_list):
#         temp = v
#         x = index_x
#         y = index_y
#         temp_list = []
#         while temp: # 当遍历到不为0的点时,遍历右下角是否为1, 为1继续遍历右下角
#             temp_list.append(str1[y])
#             if x+1 < len(record_list) and y+1 < len(record_list[0]):
#                 x += 1
#                 y += 1
#                 temp = record_list[x][y]
#             else:
#                 break
#         if temp_list:
#             ret_list.append(temp_list)
#
# print(ret_list)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0
        record_list = []

        temp_str = s[0]
        max_count = 0
        p = len(s)
        q = 0
        for index, foo in enumerate(s):
            target_list = s[index+1:p:]
            target_index = target_list.find(foo)
            if target_index > -1:
                record_list.append(index+target_index+1)
            else:
                record_list.append(len(target_list)+1)
        print(record_list)
        return max(record_list)


print(Solution().lengthOfLongestSubstring("abcabcbb"))
