# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, root):
        # write code here
        if not root:
            return True
        return self.isMirror(root.left, root.right)  # 判断看左右是否对称

    def isMirror(self, root1, root2):
        # 终止条件
        if not root1 or not root2:  # 如果两棵树中有一棵为空，则只有两棵树都为空的时候才返回true
            return not root1 and not root2
        if root1.val != root2.val:  # 如果两棵树值不同直接返回false
            return False
        # 逻辑循环体，判断树1的左子树是不是等于树2的右子树，树2的右子树是不是等于树1的左子树
        return self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)
