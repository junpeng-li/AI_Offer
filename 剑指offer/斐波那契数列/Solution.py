# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        arr = [0,1]
        while len(arr) <= n:#当数组长度小于n时，相加前两个数，然后把其添加到数组
            arr.append(arr[-1] + arr[-2])
        return arr[n]
        # write code here
