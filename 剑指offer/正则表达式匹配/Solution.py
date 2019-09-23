# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        ##先判断s和pattern是不是为空
        #若s和pattern都为空，返回true
        if len(s) == 0 and len(pattern) == 0:
            return True
        #如果s不为空，pattern为空，返回false
        elif len(s) != 0 and len(pattern) == 0:
            return False
        #如果s为空，pattern不为空，则判断
        elif len(s) == 0 and len(pattern) != 0:
            if len(pattern) > 1 and pattern[1] == '*':#若第二个字符是*，则当pattern前两个字符没存在，往后匹配
                return self.match(s,pattern[2:])
            else:
                return False
        #如果s和pattern都不为空，需要判断pattern都第二个字符是否为*
        else:
            if len(pattern) > 1 and pattern[1] == '*':#如果第二个字符是*
                #如果s和pattern第一个字符不同且pattern第一个字符不为点，则s不变
                #pattern相当与前两个字符不起作用，从第三个字符开始继续判断
                if s[0] != pattern[0] and pattern[0] != '.':
                    return self.match(s,pattern[2:])
                else:#若s和pattern第一个字符相同，且pattern为*
                    #s后移1位，pattern后移2位，相当于s[0]和pattern前两个匹配
                    #s不变，pattern后移2位，相当于把pattern前两个字符看成空
                    #pattern不变，s后移1位，相当于pattern匹配s的多位
                    return self.match(s[1:],pattern[2:]) or self.match(s,pattern[2:]) or self.match(s[1:],pattern)
            else:#如果第二个字符不是*
            #如果s和pattern的第一个字符都相同，或者pattern的第一个元素是点，则继续往后比较
                if s[0] == pattern[0] or pattern[0] == '.':
                    return self.match(s[1:],pattern[1:])
                else:
                    return False
