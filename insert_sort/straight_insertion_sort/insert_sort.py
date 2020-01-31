# -*- coding: utf-8 -*-
"""
@Time ： 2020/1/31 16:04
@Auth ： Minhang
@File ：insert_sort.py
@IDE ：PyCharm
"""

class StraightInsertionSortCls(object):

    #直接插入排序
    def straight_insertion_sort(self, target):

        #遍历数组中的所有元素，其中0号索引元素默认已排序，因此从1开始
        for x in range(1,len(target)):
            #将该元素与已排序好的前序数组依次比较，如果该元素小，则交换
            #range(x-1,-1,-1):从x-1倒序循环到0
            for i in range(x-1,-1,-1):
                #判断：如果符合条件则交换
                if target[i] > target[i+1]:
                    temp = target[i+1]
                    target[i+1] = target[i]
                    target[i] = temp

        return target

