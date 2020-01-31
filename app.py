# -*- coding: utf-8 -*-
"""
@Time ： 2020/1/31 16:32
@Auth ： Minhang
@File ：app.py
@IDE ：PyCharm
"""
from insert_sort.InsertSort import InsertSort

class MySort(InsertSort):
    pass


if __name__ == '__main__':
    target_list = [9,8,7,6,5,4,3,2,1,0,-1,-2,1,2,3,6,7,8,9]
    sort_handle = MySort()
    ret = sort_handle.straight_insertion_sort(target_list)
    print(ret)


