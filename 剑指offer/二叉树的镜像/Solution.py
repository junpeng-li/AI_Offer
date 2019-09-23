# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    #遍历，交换左右子树
    def Mirror(self, root):
        # write code here
        #temp = TreeNode(1)#先初始化一个树结构作为中间变量
        if not root:#递归结束
            return False
        #递归逻辑
        #temp = root.left
        #root.left = root.right
        #root.right = temp
        root.left,root.right = root.right,root.left#python交换时自动生成了一个中间变量
        #递归循环
        self.Mirror(root.left)
        self.Mirror(root.right)
