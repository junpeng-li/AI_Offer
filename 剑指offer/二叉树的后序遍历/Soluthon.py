# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        #后序遍历是左右根，二叉搜索树里的所有左子树要比根结点小，右子树要比根结点大
        #可以先通过后序遍历的最后一个数确定这棵树的根结点，然后用递归分别判断前后两个部分是否符合要求
        if sequence == None or len(sequence) == 0:
            return False
        length = len(sequence)
        root = sequence[length - 1]#后序遍历根结点位置
        for i in range(length):#根据根结点遍历出左右子树的分界点i，切片是左开右闭
            if sequence[i] > root:#如果数组里的这个数大于根结点，则这个数之前的数为左子树，
                break#之后的数为右子树（包含这个数）
        for j in range(i,length):#如果在比根结点大的第一个数后面还有比根结点小的数
            if sequence[j] < root:#则说明不是二叉搜索树,返回false
                return False
        #开始递归判断分好的树是不是符合这个规定，定义两个辅助的标志变量
        left = True
        if i > 0:#递归判断左子树是否符合，切片选取判断范围
            left = self.VerifySquenceOfBST(sequence[0:i])
        right = True
        if i < length - 1:
            right = self.VerifySquenceOfBST(sequence[i:-1])#不要最后一个数，因为最后一个是根结点
        #需要左右子树都满足情况的时候才是二叉搜索树的后序遍历结果
        return left and right
