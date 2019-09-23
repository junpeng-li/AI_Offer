# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        #归并排序的思路，申请一个第三个链表temp，比较两个递增链表值的大小
        #把较小的值放到temp中，然后让这个链表往下移一位
        #这个位置有值以后把temp向后移一位
        temp = ListNode(0)
        pHead = temp#移动temp以后位置就变了，就不知道头结点在那个位置，这里要保存链表头结点
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                temp.next = pHead1
                pHead1 = pHead1.next
            else:
                temp.next = pHead2
                pHead2 = pHead2.next
            temp = temp.next
        if not pHead1:
            temp.next = pHead2
        if not pHead2:
            temp.next = pHead1
        return pHead.next
