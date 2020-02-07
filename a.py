# -*- coding: utf-8 -*-
"""
@环境 ： Python3.8
@IDE  ：PyCharm
"""

import requests
import copy

class MyLastVisit(object):
    """二叉树,后序遍历,不适用于多叉树"""

    # TODO __init__
    def __init__(self, target_id):
        self.target_id = target_id # 用户输入值
        self.data_api = "https://job.xiyanghui.com/api/q1/json" # api接口
        self.stack_list1 = [] # 栈1
        self.stack_list2 = [] # 栈2

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

    def cut_tree_branch(self, node):
        """
        切树枝
        :param node: 节点 (list)
        :return: list
        """

        if self.check_node_id(node): # 栈顶找到目标id
            return node, False # 返回整个节点, 退出while死循环

        try:
            node_temp = copy.copy(node["children"])
            len_node = len(node["children"])
            i = 0
            for index in range(len_node):
                child_str = str(node_temp[index])
                if child_str.find(self.target_id) == -1: # 不存在, 删除该分支
                    node["children"].pop(index-i) # 删除分支
                    i += 1 #
        except:
            pass

        return node, True

    # TODO last_visit
    def last_visit(self, node):
        """
        后序遍历-非递归
        :param node:
        :return: bool
        """

        self.stack_list1.append(node) # 根节点压栈
        flag_stop = False

        while self.stack_list1: # 栈不为空

            stack_top = self.stack_list1.pop() # 栈顶元素出栈
            self.stack_list2.append(stack_top) # 后序遍历-输出节点

            stack_top, ret = self.cut_tree_branch(stack_top) # 切掉没用的树枝
            if not ret: # 栈顶元素找到目标id
                break # 退出while

            if self.has_left_child(stack_top): # 先左-栈顶元素有左孩子
                left_child = self.get_left_child(stack_top)
                self.stack_list1.append(left_child)  # 左孩子压栈
                if self.check_node_id(left_child): # 找到目标id
                    self.stack_list2.append(left_child) # 目标id对应的节点压栈
                    flag_stop = True #
                    break

            if self.has_right_child(stack_top): # 后右-栈顶元素有右孩子
                right_child = self.get_right_child(stack_top)
                self.stack_list1.append(right_child)  # 右孩子压栈
                if self.check_node_id(right_child): # 找到目标id
                    self.stack_list2.append(right_child) # 目标id对应的节点压栈
                    flag_stop = True #
                    break

        return flag_stop

    def search_data(self):
        """
        查找
        :return: 最终结果(str)
        """

        flag_stop = self.last_visit(self.data[0])
        if not flag_stop: # 进入男士分支, 因为根节点为空, 所以将女士和男士分开查找
            self.stack_list1 = [] # 栈清空
            self.stack_list2 = [] # 栈清空
            flag_stop = self.last_visit(self.data[1]) # 查找男士分支

        if not flag_stop: # 未找到目标id
            self.stack_list1 = []  # 栈清空
            self.stack_list2 = [{"name":"未找到"}]

        ret_list = [(foo["name"] + "") if index + 1 == len(self.stack_list2) else foo["name"] + " > " for index, foo in enumerate(self.stack_list2)]
        output_info = "".join(ret_list)
        print("输出 {}".format(output_info))

        return output_info

    # TODO run
    def run(self):

        self.get_data() # 获取api接口数据

        output_info = self.search_data() # 后序遍历

        return output_info


target_id = input("输入 ")
tree_obj = MyLastVisit(target_id)
tree_obj.run()
