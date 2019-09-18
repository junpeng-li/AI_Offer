# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        #每次取矩阵的第一行，取完以后把矩阵进行逆时针旋转,再继续取第一行如此循环
        #注意画图做题
        result = []
        while(matrix):
            result += matrix.pop(0)
            if matrix and matrix[0]:
                matrix = self.turn(matrix)
        return result
    def turn(self,matrix):
        row = len(matrix)
        col = len(matrix[0])
        num1 = []
        for i in range(col):#把列数变成行数遍历
            num2 = []
            for j in range(row):#把行数变成列数寻找
                num2.append(matrix[j][i])#取原矩阵的第一列里的所有数作为现矩阵的第一行
            num1.append(num2)#把所有行列加到矩阵里，形成新到矩阵
        num1.reverse()#使列表反向，最终完成逆时针旋转矩阵对目的
        return num1
