# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        #递归终止条件
        if not pre or not tin:
            return None
        #根据前序遍历找到根节点，并且把这个根节点从前序遍历的列表中删除
        root = TreeNode(pre.pop(0))
        #根据根节点在中序遍历中的位置分开此时的左子树和右子树
        index = tin.index(root.val)
        #递归循环体,分开左右子树
        root.left = self.reConstructBinaryTree(pre,tin[:index])
        root.right = self.reConstructBinaryTree(pre,tin[index+1:])
        return root
        # write code here
