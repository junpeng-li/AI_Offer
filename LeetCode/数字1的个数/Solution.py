class Solution:
    def countDigitOne(self, n: int) -> int:

        if n <= 0:
            return 0
        res = 0
        x = 1
        q = n
        #在个位十位等位置上循环检查一遍，看每个位置上有多少个1
        #其实就是在每个数位上都遍历一遍，看看每个位置上有多少个1
        while q != 0:
            digit = q % 10
            q //= 10
            res += q * x#高位决定的1的个数
            if digit > 1:
                res += x
            elif digit == 1:#如果digit为1，则代表着如果除了低位和高位共同决定了1的个数
                res += n%x + 1#低位决定的1的个数
            x *= 10#每次判断不同位数的1
        return res
