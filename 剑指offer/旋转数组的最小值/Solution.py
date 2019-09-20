class Solution:
    def minNumberInRotateArray(self, rotateArray):
        left = 0
        right = len(rotateArray) - 1
        if(right < 0):return 0
        while(left < right):
            mid = (left + right) >> 1 #找到中间下标
            if(rotateArray[mid] >= rotateArray[right]):#看最小值在什么位置
                left = mid + 1
            else:
                right = mid
        return rotateArray[left]
        # write code here
