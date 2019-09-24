# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        #利用快慢指针的方法，快指针每次走两步，慢指针每次走一步，如果有环两个指针必定相遇
        slow,fast,flag = pHead,pHead,False
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                flag = True#先确认链表是否有环
                break
        if not flag:#没环返回none
            return None
        else:#有环的话返回那个结点
            slow2 = pHead
            while slow2 != slow:
                slow2 = slow2.next
                slow = slow.next
            return slow2
