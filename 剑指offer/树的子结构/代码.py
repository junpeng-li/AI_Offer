# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False
        if pRoot1 != None and pRoot2 != None:#如果树为空，直接返回false，不为空才往下判断
            if pRoot1.val == pRoot2.val:#如果两个值相等，就以这个点为根结点判断是否包含pRoot2
                result = self.isPart(pRoot1,pRoot2)
            if not result:#如果这个值不相等，就再找左子树看是否有相等的点
                result = self.HasSubtree(pRoot1.left,pRoot2)
            if not result:#如果左子树也不相等，再找右子树
                result = self.HasSubtree(pRoot1.right,pRoot2)
        return result
    def isPart(self, pRoot1, pRoot2):
        if pRoot2 == None:#如果第二个树空了，证明已经判断完成了
            return True
        if pRoot1 == None or pRoot1.val != pRoot2.val:#如果第二棵树遍历没结束，第一棵树遍历结束，或者值不相等返回false
            return False
        #如果跟结点能对应上，那么就再分别去对应两棵树的左结点和右结点
        return self.isPart(pRoot1.left,pRoot2.left) and self.isPart(pRoot1.right,pRoot2.right)
