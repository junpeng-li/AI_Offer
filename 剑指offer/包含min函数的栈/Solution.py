# -*- coding:utf-8 -*-
class Solution:
    #思路：设定一个辅助栈，用来存储最小值（单调栈），以及用来做比较的辅助变量，当前的min
    #每入栈一次就和单调栈里的数比较大小，如果单调栈为空或者入栈的这个数比单调栈的栈顶小
    #则把这个数同时压入主栈和单调栈，如果入栈的数比单调栈的栈顶大，则这个数进入主栈，最小数再进入单调栈
    #出栈的时候要把主栈和单调栈里的元素都弹出
    def __init__(self):
        self.stack = []
        self.assist = []
        
    def push(self, node):
        # write code here
        min = self.min()
        if not min or node < min:
            self.assist.append(node)
        else:
            self.assist.append(min)
        self.stack.append(node)
    def pop(self):
        # write code here
        if self.stack:
            self.assist.pop()
            return self.stack.pop()
    def top(self):
        # write code here
        if self.stack:
            return self.stack[-1]
    def min(self):
        # write code here
        if self.assist:
            return self.assist[-1]
