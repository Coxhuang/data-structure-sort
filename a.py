# -*- coding: utf-8 -*-
"""
@Time ： 2020/2/4 13:37
@Auth ： Minhang
@File ：a.py
@IDE  ：PyCharm
"""
a = [
    {
        "id": 1000,
        "name": "女士",
        "children": [
            {
                "id": 1100,
                "name": "服装",
                "children": [
                    {
                        "id": 1110,
                        "name": "裙",
                        "children": [
                            {
                                "id": 1111,
                                "name": "连衣裙a"
                            },
                            {
                                "id": 1112,
                                "name": "连衣裙b"
                            },
                            {
                                "id": 1113,
                                "name": "连衣裙c"
                            }
                        ]
                    },
                    {
                        "id": 1120,
                        "name": "针织衫"
                    },{
                        "id": 1121,
                        "name": "针织衫a"
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


# stack_list = []
# target = "1113"
# output_info = []
#
# def func(L):
#
#     for item in L:
#         if "children" in item.keys(): # 非叶子节点
#             if item["id"] == int(target): # 找到id
#                 print("回溯")
#                 output_info = stack_list
#                 print("output_info:",output_info)
#                 return None
#             else: # 未找到id
#                 stack_list.append(item["children"]) # 当前字典压栈
#                 func(item["children"])  # 递归 - children
#         else: # 叶子节点
#             if item["id"] == int(target): # 找到id
#                 print("回溯")
#                 output_info = stack_list
#                 print("output_info:", output_info)
#                 return None
#             else: # 未找到id
#                 print("叶子节点 - 未找到id ")
#
#         print("=============")
#     print("-------------------")
#
# func(a)



# def func(L):
#     """"""
#     target = "1113"
#     output_info = []
#
#     for item in a:
#
#         flag_stop = False
#         node = item
#         stack_list = [item,]
#
#         while (stack_list or node):
#             print("kong")
#             # 判断节点的id
#             if node["id"] == int(target): # 相等
#                 print("回溯")
#             else: # 不相等 -> 判断是否有孩子节点
#                 if "children" in node.keys(): # 有孩子节点 -> 遍历左孩子
#
#                     while "children" in node.keys(): # 遍历左孩子至叶子节点
#                         if node["id"] == int(target):  # 相等
#                             print("回溯")
#                         else:
#                             stack_list.append(node["children"][0]) # 左孩子进栈
#
#                     # 没有左孩子 -> 栈顶元素出栈,栈顶元素右孩子进栈
#                     node = stack_list.pop()
#
#                 else: # 无孩子节点
#                     pass
#
# func(a)

import requests

class MyFirstVisit(object):
    """二叉树,先序遍历,不适用于多叉树"""

    # TODO __init__
    def __init__(self):
        self.target_id = 1112 # 用户输入值
        self.data_api = "https://job.xiyanghui.com/api/q1/json" # api接口
        self.stack_list = [] # 栈
        self.stack_output = []
        self.current_node = "" # 当前节点所在位置


    def has_left_child(self, node):
        """
        判断节点node是否有左孩子
        :param node: 节点
        :return: bool
        """

        # 先判断node是否有 children 字段
        if "children" not in node.keys():
            return False
        else:
            try:
                temp = node["children"][0]
            except: # children字段内容为空 -> 没有左孩子
                return False

        return True

    def has_right_child(self, node):
        """
        判断节点node是否有右孩子
        :param node: 节点
        :return: bool
        """

        # 先判断节点是否有左孩子
        if not self.has_left_child(node):
            # 没有左孩子 -> 没有右孩子
            return False
        else:
            # 有左孩子
            try:
                temp = node["children"][1]
            except: # children字段内容为空 -> 没有右孩子
                return False

        return True

    def get_left_child(self, node):
        """
        获取节点左孩子, 使用该函数的前提是节点有左孩子 has_left_child(node)
        :param node: 节点
        :return: 左孩子数据(dict)
        """


        return node["children"][0]

    def get_right_child(self, node):
        """
        获取节点左孩子, 使用该函数的前提是节点有右孩子 has_right_child(node)
        :param node: 节点
        :return: 右孩子数据(dict)
        """

        return node["children"][1]

    def get_node_id(self, node):
        """
        获取节点id
        :param node: 节点
        :return: id(int)
        """

        return int(node["id"])

    def get_node_name(self, node):
        """
        获取节点名
        :param node: 节点
        :return: id(int)
        """

        return node["name"]

    def get_data(self):
        """
        获取接口数据
        :return: 接口数据(list)
        """

        # self.data = requests.get(self.data_api).json()
        self.data = [
    {
        "id": 1000,
        "name": "女士",
        "children": [
            {
                "id": 1100,
                "name": "服装",
                "children": [
                    {
                        "id": 1110,
                        "name": "裙",
                        "children": [
                            {
                                "id": 1111,
                                "name": "连衣裙a"
                            },
                            {
                                "id": 1112,
                                "name": "连衣裙b"
                            }
                        ]
                    },
                    {
                        "id": 1120,
                        "name": "针织衫"
                    },{
                        "id": 1121,
                        "name": "针织衫a"
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

        return None

    def check_node_id(self, node):
        """
        判断节点id是否是我们要找的id
        :param node: 节点
        :return: bool
        """

        if node["id"] == self.target_id:
            return True
        return False

    # TODO first_visit
    def first_visit(self):
        """先序遍历"""


        # 遍历接口数据, 因为根节点数据为空, 所以分别遍历根节点的左右孩子
        for item in self.data:
            print(item)
            self.stack_list.append(item) # 根节点左孩子压栈
            self.current_node = item # 游标移动到根节点的左孩子

            while self.stack_list or self.current_node:
                # 只要栈不为空且当前节点的值不为空, 就一直循环遍历

                while self.current_node:
                    # 一直遍历到左孩子为空为止
                    if self.check_node_id(self.current_node):
                        # 找到目标值
                        print("回溯")
                        print(self.stack_list)
                    else:
                        # 没有找到目标值
                        if self.has_left_child(self.current_node):
                            # 有左孩子
                            # 游标移动到左孩子
                            self.current_node = self.get_left_child(self.current_node)
                            # 左孩子数据压栈
                            self.stack_list.append(self.current_node)
                        else:
                            # 没有左孩子
                            # 游标置为空
                            self.current_node = {}

                # 左孩子为空, 栈顶元素出栈, 游标移动到栈顶元素的右孩子
                self.current_node = self.stack_list.pop()
                if self.has_right_child(self.current_node):
                    # 有右孩子
                    # 游标移动到右孩子
                    self.current_node = self.get_right_child(self.current_node)
                else:
                    # 没有右孩子
                    # 游标置为空
                    self.current_node = {}

        return None

    # TODO run
    def run(self):

        # 获取接口数据
        self.get_data()
        # print(self.data)
        # 先序遍历
        self.first_visit()
        print(self.stack_list)
        return None



tree_obj = MyFirstVisit()
tree_obj.run()
