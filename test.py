# -*- coding: utf-8 -*-
"""
@Time ： 2020/2/2 00:13
@Auth ： Minhang
@File ：test.py
@IDE  ：PyCharm
"""

def fib(max_val):
    a, b, n = 0, 1, max_val
    while n:
        a, b = b, a+b
        n -= 1
    return b

n = 3 # 台阶数
ret = n if n <= 2 else fib(n)
print(ret)
