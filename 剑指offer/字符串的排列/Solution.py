# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        #如果字符串数少于1个，直接返回。
        #固定第一个元素，其他的进行全排列递归求解
        if len(ss) <= 1:
            return ss
        ans = []
        for i in range(len(ss)):
            #固定第一个元素，对其他元素全排列求解
            #利用map函数的特性，每次返回一个组合好的字符串
            for j in map(lambda x: ss[i] + x,self.Permutation(ss[:i]+ss[i+1:])):
                if j not in ans:
                    ans.append(j)
        return ans


