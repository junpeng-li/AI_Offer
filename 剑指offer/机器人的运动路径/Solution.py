class Solution:
    def movingCount(self, threshold, rows, cols):
        self.row, self.col = rows, cols
        self.dict = set()#用来存储走过的路径
        self.search(threshold, 0, 0)
        return len(self.dict)
 
    def judge(self, threshold, i, j):#判断行列坐标之和是不是大于K
        return sum(map(int, list(strw(i)))) + sum(map(int, list(str(j)))) <= threshold
 
    def search(self, threshold, i, j):
        if not self.judge(threshold, i, j) or (i, j) in self.dict:#递归终止条件
            return
        self.dict.add((i, j))#未走过的加到dict里
        if i != self.row - 1:#循环体，从最左上角开始往右和下遍历，确保每个符合条件的都被遍历到
            self.search(threshold, i + 1, j)
 
        if j != self.col - 1:
            self.search(threshold, i, j + 1)
