# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    # 首先把结点进行复制，把复制的结点链接在原链表的每一个对应结点后边
    # 然后遍历链表，如果有随机指针，则复制链表的随机指针为这个原随机指针的下一个位置。
    def Clone(self, pHead):
        # write code here
        if pHead == None:
            return None
        # 1.复制结点
        dummy = pHead  # 记录头结点地置
        while dummy:
            dummynext = dummy.next
            copynode = RandomListNode(dummy.label)
            copynode.next = dummynext
            dummy.next = copynode
            dummy = dummynext
        # 2.处理随机指针，复制链表的随机指针为原链表随机指针的下一个位置
        dummy = pHead  # 继续从最初的头结点开始
        while dummy:
            dummyrandom = dummy.random
            copynode = dummy.next
            if dummyrandom:
                copynode.random = dummyrandom.next
            dummy = copynode.next  # 每两个原链表结点中间隔着一个复制链表结点
        # 3.把复制好的链表和原链表切分开
        dummy = pHead
        copyHead = pHead.next
        while dummy:
            copyNode = dummy.next
            dummynext = copyNode.next
            dummy.next = dummynext
            if dummynext:
                copyNode.next = dummynext.next
            else:
                copyNode = None
            dummy = dummynext
        return copyHead
