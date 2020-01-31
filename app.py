# -*- coding: utf-8 -*-
"""
@Time ： 2020/1/31 16:32
@Auth ： Minhang
@File ：app.py
@IDE  ：PyCharm
"""
from insert_sort.insert_sort import InsertSort
from selection_sort.selection_sort import SelectionSort
from swap_sort.swap_sort import SwapSort

class MySort(InsertSort, SelectionSort, SwapSort):
    pass


if __name__ == '__main__':
    target_list = [9,8,7,6,5,4,3,2,1,0,-1,-2,1,2,3,6,7,8,9]
    sort_handle = MySort()
    ret = sort_handle.straight_insertion_sort(target_list) # 插入排序-直接插入排序
    print(ret)
    ret = sort_handle.shells_method(target_list) # 插入排序-希尔排序
    print(ret)
    ret = sort_handle.straight_selection_sort(target_list) # 选择排序-直接选择排序
    print(ret)
    ret = sort_handle.heap_sort(target_list)  # 选择排序-堆排序
    print(ret)
    ret = sort_handle.bubble_sort(target_list)  # 交换排序排序-冒泡排序
    print(ret)


