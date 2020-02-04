# -*- coding: utf-8 -*-
"""
@Time ： 2020/2/2 00:13
@Auth ： Minhang
@File ：test.py
@IDE  ：PyCharm
"""


catalog_list = [
    {
        "id": 1000,
        "name": "女士",
        "children": [
            {
                "id": 1230,
                "name": "服装",
                "children": [
                    {
                        "id": 2191,
                        "name": "裙",
                        "children": [
                            {
                                "id": 1111,
                                "name": "连衣裙"
                            }
                        ]
                    },
                    {
                        "id": 1120,
                        "name": "针织衫"
                    }
                ]
            },
            {
                "id": 1200,
                "name": "鞋履",
                "children": [
                    {
                        "id": 1210,
                        "name": "高跟鞋"
                    },
                    {
                        "id": 1220,
                        "name": "靴子"
                    }
                ]
            }
        ]
    },
    {
        "id": 2000,
        "name": "男士",
        "children": [
            {
                "id": 2100,
                "name": "服装",
                "children": [
                    {
                        "id": 4110,
                        "name": "上衣",
                        "children": [
                            {
                                "id": 2111,
                                "name": "T恤"
                            },
                            {
                                "id": 2112,
                                "name": "POLO衫"
                            }
                        ]
                    },
                    {
                        "id": 2124,
                        "name": "西装"
                    }
                ]
            },
            {
                "id": 3212,
                "name": "鞋履",
                "children": [
                    {
                        "id": 2210,
                        "name": "平底鞋"
                    },
                    {
                        "id": 2220,
                        "name": "运动鞋",
                        "children": [
                            {
                                "id": 2221,
                                "name": "篮球鞋"
                            }
                        ]
                    }
                ]
            }
        ]
    }
]

# input_info = input("请输入id:")
input_info = "1234"
input_info_list = [int(foo) for foo in list(input_info)]
gender_id = input_info_list[0] * 1000
output_info = "" # 输出内容
output_info_list = []

# for item in catalog_list:
#     # 获取性别类-字典
#     if gender_id == item["id"]:
#         print(item)
#         output_info = "".join((item["name"]," >"))
#         children_dict = item["children"]
#
# print(output_info)


def func(target_list):
    if isinstance(target_list,list):
        for items in target_list:
            if "children" in items.keys():
                output_info_list.append(items["name"])
                return func(items["children"])
            else:
                return None
    else:
        pass

print(catalog_list)
func(catalog_list)
print(output_info_list)