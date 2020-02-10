# -*- coding: utf-8 -*-
"""
@Time ： 2020/1/31 16:04
@Auth ： Minhang
@File ：straight_insertion_sort.py
@IDE  ：PyCharm
"""

class StraightInsertionSortCls(object):
    """直接插入排序"""

    def straight_insertion_sort(self, target):

        #遍历数组中的所有元素，其中0号索引元素默认已排序，因此从1开始
        for x in range(1, len(target)):
            #将该元素与已排序好的前序数组依次比较，如果该元素小，则交换
            #range(x-1,-1,-1):从x-1 倒序(已排序列从右往左) 循环到0 [x-1,-1)
            for i in range(x-1, -1, -1):
                #判断：如果符合条件则交换
                if target[i] > target[i+1]:
                    target[i], target[i+1] = target[i+1], target[i]
                else:
                    break # 当左边的数小于右边的, 本轮到此为止

        return target

if __name__ == "__main__":
    obj = StraightInsertionSortCls()
    ret = obj.straight_insertion_sort([9,8,7,6,5,4,3,2,1,0,-1,-2,1,2,3,6,7,8,9])
    print(ret)

