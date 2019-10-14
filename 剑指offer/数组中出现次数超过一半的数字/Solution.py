# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        #思路1，可以对数组进行排序，然后针对排序过后对数组，取出中间对那个数字，必定是出现次数超过数组长度一半的
        #思路2，设置一个辅助变量计算数字出现的从次数，一个辅助变量保存当前这个数。
        #从第一个数开始遍历，如果后面的这个数和第一个数相同，则次数变量加一，如果不同次数变量减一
        #若次数变量为0的时候，储存数字的变量减一换成后面的这个数，然后把次数变量置1。
        #遍历结束，最终保存在辅助数组里的那个数就是要求的数，再判断一下这个数是不是在数组中出现的次数满足要求即可
        if numbers == None:
            return 0
        times = 1
        ans = numbers[0]
        n = len(numbers)
        for i in range(1,n):
            if times == 0:
                ans = numbers[i]
                times = 1
            elif ans == numbers[i]:
                times += 1
            else:
                times -= 1
        import collections
        return ans if collections.Counter(numbers)[ans] * 2 > n else 0
        
