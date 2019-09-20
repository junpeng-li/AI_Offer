# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):#初始化两个栈
        self.stack1 = []
        self.stack2 = []
    def push(self, node):#压入只需要往堆栈1里存就可以了
        self.stack1.append(node)
        # write code here
    def pop(self):#弹出需要把堆栈1的数字按顺序压入堆栈2以后再对堆栈2进行pop操作即可
        if self.stack2:#判断堆栈2里有没有数
            return self.stack2.pop()
        elif not self.stack1:#堆栈1是否为空
            return None
        else:#当堆栈1有数，堆栈2没数的情况
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
