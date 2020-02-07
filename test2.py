# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
@环境 ： Python3.8
@IDE  ：PyCharm
"""

import requests
import re

class RateConverter(object):

    def __init__(self, money):

        # 去掉左边的空格--防呆
        self.money = money.lstrip(" ")
        self.currency_dict = {"$":"USD","£":"GBP","€":"EUR","HK$":"HKD","¥":"JPY"}
        # 实时汇率api接口, 美元兑换其他币种的汇率
        self.rate_api = "https://app-cdn.2q10.com/api/v2/currency"

    def get_currency(self):
        """
        获取货币种类
        :return: 返回货币种类(非特殊字符)
        """

        index = self.money.index(re.search('\d+', self.money).group()[0])
        # 如果是缩写
        currency = self.money[0:index]
        if currency in self.currency_dict.keys():
            return self.currency_dict[currency]

        return currency

    def get_amount(self):
        """
        获取金额
        :return: 金额(float)
        """

        index = self.money.index(re.search('\d+', self.money).group()[0])
        # 只保留数字和小数点
        amount = "".join(list(filter(lambda ch: ch in "0123456789.", self.money[index:-1])))

        return float(amount)

    def get_rate(self):
        """
        获取实时汇率
        :return: 汇率(dict)
        """

        rate_data = requests.get(self.rate_api).json().get("rates",{})

        return rate_data

    def exchange_money(self):
        """
        转换成人民币
        :return: 人民币(float)
        """

        # 汇率
        rate_data = self.get_rate()
        # 货币种类
        currency = self.get_currency()
        # 其他货币兑美元汇率
        rate_to_usd = rate_data.get(currency,1)
        # 人民币兑美元汇率
        rate_usd_to_cny = rate_data.get("CNY",7)
        amount = self.get_amount()

        return float(rate_to_usd) * amount * float(rate_usd_to_cny)

    def check_input_info(self):
        """
        校验输入值
        :return: bool
        """

        # 货币种类
        currency = self.get_currency()
        if currency not in ["USD","GBP","EUR","HKD","JPY"]:
            return False

        return True

    def run(self):

        check_ret = self.check_input_info()
        if check_ret:
            print("输出 {}".format(self.exchange_money()))
        else:
            print("只考虑币种：美元(USD, $)，英镑(GBP, £)，欧元(EUR, €)，港币(HKD, HK$)，日元(JPY, ¥)")

        return None

input_info = input("输入 ")
rate_obj = RateConverter(input_info)
rate_obj.run()





