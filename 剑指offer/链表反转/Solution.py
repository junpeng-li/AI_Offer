# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        #定义两个指针，分别记录当前位置和前一个位置
        #反转的时候需要把当前位置的结点指向前一个位置
        cur,pre = pHead,None
        #只要当前结点不为空就继续反转
        while cur:
            #要用一个临时变量去记录cur的下一个位置
            #当cur指向前一个结点当时候，他已经不知道下一个结点当位置了
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        #当cur为空当时候意味着已经是最后当结点，此时pre就指向头结点位置
        return pre
