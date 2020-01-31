# -*- coding: utf-8 -*-
"""
@Time ： 2020/1/31 20:59
@Auth ： Minhang
@File ：straight_selection_sort.py
@IDE  ：PyCharm
"""

class StraightSelectionSort(object):
    """直接选择排序"""

    def straight_selection_sort(self, target):
        # 依次遍历序列中的每一个元素
        for x in range(0, len(target)):
            # 将当前位置的元素定义此轮循环当中的最小值
            minimum = target[x]
            # 将该元素与剩下的元素依次比较寻找最小元素
            for i in range(x + 1, len(target)):
                if target[i] < minimum:
                    temp = target[i]
                    target[i] = minimum
                    minimum = temp
                    # 将比较后得到的真正的最小值赋值给当前位置
            target[x] = minimum

        return target