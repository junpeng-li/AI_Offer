class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #思路就是递归搜索遍历，上下左右四个方向，看是否有1,若有1则判断四个方向看有多少1，把所有联通的1算一个岛屿
        #在搜索遍历的时候，注意边界条件，然后每遍历过一个位置就把这个位置变1，保证这个位置不会被重复遍历
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid,i,j)
                    count+=1
        return count
    def dfs(self,grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j - 1)
