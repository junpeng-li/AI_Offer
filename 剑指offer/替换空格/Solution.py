# -*- coding:utf-8 -*-
import re
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        #s = re.sub(' ','%20',s)#正则的方式替换空格
        #return s
        string = ''
        for i in s:
            if i == ' ':
                string += '%20'
            else:
                string += i
        return string
        # write code here
