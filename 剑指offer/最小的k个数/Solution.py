class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if len(tinput) < k:
            return []
        return self.quick_sort(tinput)[0:k]#返回快排后的结果
    def quick_sort(self,tinput):
        if len(tinput) < 2:
            return tinput[:]
        mid_index = 0
        mid = tinput[mid_index]
        left = self.quick_sort([i for i in tinput[mid_index+1:] if i <= tinput[mid_index]])
        right = self.quick_sort([i for i in tinput[mid_index+1:] if i > tinput[mid_index]])
        return left + [mid] + right
