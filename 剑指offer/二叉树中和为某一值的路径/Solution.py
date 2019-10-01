# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    #分别设定一个用来存放答案和路径的辅助数组，主函数调用dfs函数，输出路径
    #一个辅助变量用来和expectNumber比对
    #dfs函数是用来寻找遍历路径的，采用excepNumber逐级递减的方式去判断路径和是否相等
    def __init__(self,):
        self.answer = []#初始化一个答案数组
        self.path = []#存放路径
    def FindPath(self, root, expectNumber):
        # write code here
        if root == None:
            return []
        self.path.append(root.val)#把当前这个路径加到path里
        expectNumber -= root.val#把路径上的值减去
        #递归终止条件：是否还有左右子树，exceptNumber是否为0
        if not root.left and not root.right and not expectNumber:
            self.answer.append(self.path[:])#要把值传给answer，不能把内存地址传给answer，否则pop的时候会answer跟着一起pop掉
        #递归循环处理左右子树
        if root.left != None:
            self.FindPath(root.left,expectNumber)
        if root.right != None:
            self.FindPath(root.right,expectNumber)
        self.path.pop()#清空当前遍历的结果，用来继续存放下一个结果，所有的叶结点都要弹出去
        #弹出以后不用再加回target，因为在最后的数里target
        return self.answer
