# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        if pHead.val == pHead.next.val:#如果当前的节点值和下个节点值重复，则往下找看还有没有重复的
            p = pHead.next.next
            #while p and p.val==pHead.val
            while p and p.val == pHead.val:#当还有值并且下个值等于当前值的时候继续往下找
                p = p.next#直到没有重复值,注意p一直会在动态变化中，比较的时候用pHead的值，不会变化
            return self.deleteDuplication(p)#继续处理以p为头节点的情况
        #如果当前节点值和下个节点值不重复，则处理以下个节点值为头结点的情况
        pHead.next = self.deleteDuplication(pHead.next)
        return pHead
        # write code here
