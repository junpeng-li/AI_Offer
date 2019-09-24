# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        #一共需要判断三种特殊情况，分别是e，符号位,小数点
        if len(s) <= 0:
            return False
        #分别对e，符号位，小数点，设置三个标志位
        has_e = False
        has_sign = False
        has_point = False
        for i in range(len(s)):
            #对于出现e来说，e不能出现两次，也不能出现在最后，因为e后面要跟数字
            if s[i] == 'e' or s[i] =='E':
                if has_e:
                    return False
                else:
                    has_e = True
                    if i == len(s) - 1:
                        return False
            #对于符号位来说，如果出现了两次，第二次只能出现在e之后
            #如果符号位第一次出现，若不是第一个位置，则只能e之后
            elif s[i] == '+' or s[i] == '-':
                if has_sign:
                    #此位置注意，and是从左到右返回第一个为假的数据，若没有则返回最后一个数
                    #or是从做到右返回第一个为真的数据，若没有则返回最后一个数
                    if s[i - 1] != 'e' and s[i - 1] != 'E':
                        return False
                else:
                    has_sign = True
                    if i > 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                        return False
            #对于小数点来说，小数点不能第二次出现，如果出现了e就不能出现小数点
            #如果是第一次出现小数点，小数点前也不能有e
            #即小数点前不能有小数点和e
            elif s[i] == '.':
                if has_e:
                    return False
                elif has_point:
                    return False
                else:
                    has_point = True
            else:#其余要判断是否在0-9范围内
                if s[i] < '0' or s[i] > '9':
                    return False
        return True



