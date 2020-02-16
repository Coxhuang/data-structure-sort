# -*- coding: utf-8 -*-
"""
@Time ： 2020/1/31 20:40
@Auth ： Minhang
@File ：shells_method.py
@IDE  ：PyCharm
"""


class ShellsMethodCls(object):
    """希尔排序"""

    def shells_method(self, target):
        # 初始化gap值，此处利用序列长度的一般为其赋值
        gap = (int)(len(target) / 2)
        # 第一层循环：依次改变gap值对列表进行分组
        while gap >= 1:
            for x in range(len(target)):
                y = x
                while y >= gap and target[y - gap] > target[y]:  # 在每一组里面进行直接插入排序
                    target[y], target[y - gap] = target[y - gap], target[y]
                    y -= gap
            gap //= 2  # 更新步长
            
        return target

if __name__ == "__main__":
    oby = ShellsMethodCls()
    ret = oby.shells_method([9,8,-10,7,6,5,4])
    print(ret)