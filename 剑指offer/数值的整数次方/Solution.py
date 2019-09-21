# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        value = 1
        if base == 0 and exponent == 0:
            return False
        if exponent == 0:
            return value
        for i in range(abs(exponent)):
            value *= base
        if exponent < 0:
            value = 1/value
        return value
