# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        #设定快慢两个指针，先让快指针走k步，然后再让慢指针和快指针一起走
        #当快指针走到none的时候，慢指针指向的数就是倒数第k个
        fast,slow = head,head
        for i in range(k):
            if not fast:#如果还没走到k步就走完了，返回none
                return None
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow
