# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix:
            return False
        if not path:
            return True
        x = [list(matrix[cols*i:cols*i+cols]) for i in range(rows)]#把列表变换成矩阵
        for i in range(rows):#遍历矩阵看是否有符合条件的情况
            for j in range(cols):
                if self.exist_path(x,i,j,path):
                    return True
        return False
    def exist_path(self,matrix,i,j,p):
        if matrix[i][j] == p[0]:#每次取字符串的第一个字母，若匹配则开始在这个字母周围寻找看是否有符合条件的字母
            if not p[1:]:#若找到匹配的则继续往下一个字母遍历，直到p为空
                return True
            matrix[i][j] = ' '#把字符串中已经遍历过的字母变为空格
            if i > 0 and self.exist_path(matrix, i-1, j, p[1:]):
                return True
            if i < len(matrix)-1 and self.exist_path(matrix, i+1, j ,p[1:]):
                return True
            if j > 0 and self.exist_path(matrix,i,j - 1,p[1:]):
                return True
            if j < len(matrix[0]) - 1 and self.exist_path(matrix,i,j + 1,p[1:]):
                return True
            matrix[i][j] = p[0]#如果这个遍历过的字母周围没有符合条件的情况，则把其恢复原来的样子继续往后遍历
            return False
        else:
            return False
