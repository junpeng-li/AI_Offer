# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        #思路：设定一个辅助队列存入头结点，用来遍历树；一个辅助数组用来存放结果
        #每次取辅助队列里的第一个数，把它的值传入到结果队列里，然后判断看这个结点有没有左子树或者右子树
        #如果有，则把这个树的左子树或右子树放入队列的后面继续遍历，队列为空的时候即为遍历完成
        queue = [root]
        result = []
        if not root:
            return []
        while len(queue) > 0:
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result
