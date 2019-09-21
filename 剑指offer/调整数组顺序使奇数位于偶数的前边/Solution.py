# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        #空间复杂度O(n)的解法
        even,odd=[],[]
        for i in array:
            if i%2:
                odd.append(i)
            else:
                even.append(i)
        return odd + even
#解法二
'''class Solution(object):
    def reOrderArray(self, array):
        #设定两个指针，一个从前往后走，一个从后往前走
        #保证第一个指针的前边全是奇数，第二个指针的后边全是偶数
        i = 0
        j = len(array) - 1
        while(i <= j):
            while(array[i] % 2 == 1):
                i += 1
            while(array[j] % 2 == 0):
                j -= 1
            if(i < j):#当两个指针还没有相遇的时候进行交换
                array[i],array[j] = array[j],array[i]
                '''
