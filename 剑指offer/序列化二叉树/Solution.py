# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        #以前序遍历序列化
        if root == None:
            return '#'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)
    def Deserialize(self, s):
        # write code here
        #先把字符串转换成一个列表，然后按前序遍历的思路把树遍历出来即可
        tlist = s.split(',')
        return self.deserialize(tlist)
    def deserialize(self,tlist):
        if tlist == None:
            return None
        val = tlist.pop(0)
        root = None
        if val != '#':
            root = TreeNode(int(val))
            root.left = self.deserialize(tlist)
            root.right= self.deserialize(tlist)
        return root
