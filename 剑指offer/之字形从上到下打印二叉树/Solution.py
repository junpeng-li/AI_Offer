# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        #从上往下分行打印，分奇数行和偶数行两种打印方式
        #奇数行正向打印，偶数行反向打印
        result=[]#存储最终结果
        cur_result=[]#存储分行结果
        queue = [pRoot]# 存储头结点的辅助队列
        cur_number = 1#计算当前层遍历结点数
        next_number = 0#下一层需要遍历的结点
        cur_row = 1#记录当前是第几行
        if not pRoot:
            return []
        while len(queue) > 0:
            node = queue.pop(0)
            cur_result.append(node.val)
            cur_number -= 1
            if node.left:
                queue.append(node.left)
                next_number += 1
            if node.right:
                queue.append(node.right)
                next_number += 1
            if cur_number == 0:
                if cur_row % 2 == 0:
                    result.append(cur_result[::-1])
                else:
                    result.append(cur_result)
                cur_number = next_number
                next_number = 0
                cur_result = []
                cur_row += 1
        return result
