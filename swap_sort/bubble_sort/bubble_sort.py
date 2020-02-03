# -*- coding: utf-8 -*-
"""
@Time ： 2020/1/31 22:01
@Auth ： Minhang
@File ：bubble_sort.py
@IDE  ：PyCharm
"""


class BubbleSort(object):
    """冒泡排序"""

    def bubble_sort(self, target):
        length = len(target)
        # 序列长度为length，需要执行length-1轮交换
        for i in range(1, length):
            # 对于每一轮交换，都将序列当中的左右元素进行比较
            # 每轮交换当中，由于序列最后的元素一定是最大的，因此每轮循环到序列未排序的位置即可
            for j in range(0, length-i):
                if target[j] > target[j+1]:
                    target[j], target[j+1] = target[j+1], target[j]

        return target