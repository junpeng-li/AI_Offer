# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        n = len(numbers)
        for i in range(n):
            index = numbers[i]
            if index >= n:#每次加N可能会导致未被遍历过的数加n，这里的目的是
                index -= n#如果出现未被遍历过的数>=n的情况，则减去n使其在这次循环中恢复原值，但是数组里的值并没产生变化
            if numbers[index] >= n:
                duplication[0] = index
                return True
            numbers[index] += n
        return False
        # write code here 相当于把以出现过的数字作为下标的值+n,继续循环
        #，每次判断以循环数字为下标的值是否大于n，若大于则返回，若不大于继续加n循环。
