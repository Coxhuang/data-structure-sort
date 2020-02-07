# -*- coding: utf-8 -*-
"""
@Time ： 2020/2/4 13:37
@Auth ： Minhang
@File ：a.py
@IDE  ：PyCharm
"""

import requests

class MyLastVisit(object):
    """二叉树,后序遍历,不适用于多叉树"""

    # TODO __init__
    def __init__(self, target_id):
        self.target_id = target_id # 用户输入值
        self.data_api = "https://job.xiyanghui.com/api/q1/json" # api接口
        self.stack_list1 = [] # 栈
        self.stack_list2 = [] # 栈
        self.stack_output = []
        self.current_node = "" # 当前节点所在位置
        self.stop = False


    def has_left_child(self, node):
        """
        判断节点node是否有左孩子
        :param node: 节点 (dict)
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

        self.data = requests.get(self.data_api).json()
#         self.data = [
#     {
#         "id": 1000,
#         "name": "女士",
#         "children": [
#             {
#                 "id": 1100,
#                 "name": "服装",
#                 "children": [
#                     {
#                         "id": 1110,
#                         "name": "裙",
#                         "children": [
#                             {
#                                 "id": 1111,
#                                 "name": "连衣裙a"
#                             },
#                             {
#                                 "id": 1112,
#                                 "name": "连衣裙b"
#                             }
#                         ]
#                     },
#                     {
#                         "id": 1120,
#                         "name": "针织衫"
#                     },{
#                         "id": 1121,
#                         "name": "针织衫a"
#                     }
#                 ]
#             },
#             {
#                 "id": 1200,
#                 "name": "鞋履",
#                 "children": [
#                     {
#                         "id": 1210,
#                         "name": "高跟鞋"
#                     },
#                     {
#                         "id": 1220,
#                         "name": "靴子"
#                     }
#                 ]
#             }
#         ]
#     },
#     # {
#     #     "id": 2000,
#     #     "name": "男士",
#     #     "children": [
#     #         {
#     #             "id": 2100,
#     #             "name": "服装",
#     #             "children": [
#     #                 {
#     #                     "id": 4110,
#     #                     "name": "上衣",
#     #                     "children": [
#     #                         {
#     #                             "id": 2111,
#     #                             "name": "T恤"
#     #                         },
#     #                         {
#     #                             "id": 2112,
#     #                             "name": "POLO衫"
#     #                         }
#     #                     ]
#     #                 },
#     #                 {
#     #                     "id": 2124,
#     #                     "name": "西装"
#     #                 }
#     #             ]
#     #         },
#     #         {
#     #             "id": 3212,
#     #             "name": "鞋履",
#     #             "children": [
#     #                 {
#     #                     "id": 2210,
#     #                     "name": "平底鞋"
#     #                 },
#     #                 {
#     #                     "id": 2220,
#     #                     "name": "运动鞋",
#     #                     "children": [
#     #                         {
#     #                             "id": 2221,
#     #                             "name": "篮球鞋"
#     #                         }
#     #                     ]
#     #                 }
#     #             ]
#     #         }
#     #     ]
#     # }
# ]

        return None

    def check_node_id(self, node):
        """
        判断节点id是否是我们要找的id
        :param node: 节点
        :return: bool
        """

        if str(node["id"]) == str(self.target_id):
            return True
        return False

    def get_node_data(self, node):
        """
        获取节点数据
        :return: children(list)
        """

        data = node.get("children",[])
        return data

    # TODO last_visit
    def last_visit(self, node):
        """
        后序遍历-非递归
        :param node:
        :return: bool
        """

        # node = self.data[0] # 获取左孩子根节点数据
        self.stack_list1.append(node) # 压栈
        flag_stop = False

        while self.stack_list1:

            stack_top = self.stack_list1.pop() # 栈顶元素出栈
            self.stack_list2.append(stack_top)
            if self.has_right_child(stack_top): # 栈顶元素有右孩子
                right_child = self.get_right_child(stack_top)
                self.stack_list1.append(right_child)  # 右孩子压栈
                if self.check_node_id(right_child):
                    self.stack_list2.append(right_child)
                    flag_stop = True
                    break

            if self.has_left_child(stack_top): # 栈顶元素有左孩子
                left_child = self.get_left_child(stack_top)
                self.stack_list1.append(left_child)  # 左孩子压栈
                if self.check_node_id(left_child):
                    self.stack_list2.append(left_child)
                    flag_stop = True
                    break

        return flag_stop

    def search_data(self):
        """
        查找
        :return:
        """

        flag_stop = self.last_visit(self.data[0])
        if not flag_stop:
            self.stack_list1 = []
            self.stack_list2 = []
            self.last_visit(self.data[1])

        return None


    # TODO run
    def run(self):

        self.get_data() # 获取接口数据

        self.search_data() # 后序遍历

        ret_list = [(foo["name"]+"") if index+1 == len(self.stack_list2) else foo["name"]+" > " for index,foo in enumerate(self.stack_list2)]
        output_info = "".join(ret_list)
        print("输出 {}".format(output_info))

        return output_info


target_id = input("输入 ")
tree_obj = MyLastVisit(target_id)
tree_obj.run()
