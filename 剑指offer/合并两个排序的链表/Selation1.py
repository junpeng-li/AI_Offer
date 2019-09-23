
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    temp = ListNode(0)
    head = temp
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 is None:
            self.temp.next = pHead2#终止条件
            return self.head.next#如果phead2直接为0，则按正常返回
        if pHead2 is None:
            self.temp.next = pHead1
            return self.head.next
        if pHead1.val <= pHead2.val:
            self.temp.next = pHead1
            self.temp = self.temp.next
            self.Merge(pHead1.next,pHead2)
        else:
            self.temp.next = pHead2
            self.temp = self.temp.next
            self.Merge(pHead1,pHead2.next)
        return self.head.next #递归是从最里边一层层返回，最外边返回的是第一个结点
