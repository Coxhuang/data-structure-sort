# -*- coding: utf-8 -*-
"""
@Time ： 2020/1/31 21:59
@Auth ： Minhang
@File ：swap_sort.py
@IDE  ：PyCharm
"""
from swap_sort.bubble_sort.bubble_sort import BubbleSort
from swap_sort.quick_sort.quick_sort import QuickSort

class SwapSort(BubbleSort, QuickSort):
    """交换排序"""