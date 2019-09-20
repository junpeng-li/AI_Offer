class Solution:
    def NumberOf1(self, n):
        count = 0
        if(n < 0):#求负数的补码
            n = n&0xffffffff
        while(n):
            count += 1
            n = n&(n - 1)#把减1后的数与上自己，就把这个整数最右边的数变成了1，有多少1就能进行多少次操作
        return count
        # write code here
