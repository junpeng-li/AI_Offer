# -*- coding:utf-8 -*-
class Solution:#尽可能的选3，直到剩下的是2或者4,为最佳方案
    def cutRope(self, number):
        #如果长度小于3，直接返回数
        if(number <= 3):return number - 1
        val = 1
        #先对其做减2或4的操作，让剩下的数可以整除3
        if(number % 3 ==1):
            val *= 4
            number -= 4
        if(number % 3 ==2):
            val *= 2
            number -= 2
        #遍历可以整除3的数
        while(number):
            val *= 3
            number -= 3
        return val
        # write code here
