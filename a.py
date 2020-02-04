# -*- coding: utf-8 -*-
"""
@Time ： 2020/2/4 13:37
@Auth ： Minhang
@File ：a.py
@IDE  ：PyCharm
"""
import re
money = "sdmefipf89r832eiwhd"
print(str(filter(lambda ch: ch in "0123456789.", money)))