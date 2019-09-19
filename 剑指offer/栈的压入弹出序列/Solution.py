# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        #思路：需要一个辅助栈，去还原压栈过程。把压栈顺序依次压入辅助栈
        #看辅助栈的最后一个数是不是和弹出序列的第一个数相等，如果相等把这两个数弹出
        #如果不等，则继续压栈，如果压栈完成辅助栈还不是空，则说明这个序列不是弹出序列。
        if len(pushV) != len(popV):
            return False
        stack = []
        j = 0
        for i in range(len(pushV)):
            stack.append(pushV[i])
            #当popV还没有遍历完成，并且当前辅助序列的最后一个数等于popV的第一个数时
            while j < len(popV) and stack[len(stack) - 1] == popV[j]:
                stack.pop()
                j += 1 #若出栈一次，popV位置往后移动一次
        if stack:
            return False
        else:
            return True
