# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
#只需要判断这个结点的身份否是左结点或者根结点即可，因为右结点的情况包含在这两种情况里
class Solution:
    def GetNext(self, pNode):
        if pNode == None: return None
        #先判断看有没有右子树，如果有右子树，则直接返回右子树里最左边的那个数
        if pNode.right:
            p = pNode.right
            while p.left:
                p = p.left
            return p
        #没有右子树的情况，需要看这个结点下一个结点的左结点是不是当前这个结点
        while pNode.next:
            if(pNode.next.left == pNode):
                return pNode.next
            pNode = pNode.next
        return None#，如果只是右结点，后续没有值，返回的是none
        # write code here
