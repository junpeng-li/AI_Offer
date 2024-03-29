## 一.岛屿数量
### 1.[题目描述](https://leetcode-cn.com/problems/number-of-islands/submissions/)
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。
你可以假设网格的四个边均被水包围。
### 2.解题思路
这个题其实就是找联合在一起的1有多少块，再说的直白一点就是寻找被0隔开了的1分散了几个地方。所以我们可以通过遍历矩阵的行和列去检查有多少1是联合在一起的，
递归搜索的时候，寻找当前这个值上下左右四个位置的值就可以了，如果是1就把这个值变成0 ，防止被再次遍历。  

### 此思路来自[jyd](https://leetcode-cn.com/problems/number-of-islands/solution/number-of-islands-shen-du-you-xian-bian-li-dfs-or-/)
dfs方法： 设目前指针指向一个岛屿中的某一点 (i, j)，寻找包括此点的岛屿边界。
从 (i, j) 向此点的上下左右 (i+1,j),(i-1,j),(i,j+1),(i,j-1) 做深度搜索。  
终止条件：  
(i, j) 越过矩阵边界;  
grid[i][j] == 0，代表此分支已越过岛屿边界。  
搜索岛屿的同时，执行 grid[i][j] = '0'，即将岛屿所有节点删除，以免之后重复搜索相同岛屿。  
主循环：  
遍历整个矩阵，当遇到 grid[i][j] == '1' 时，从此点开始做深度优先搜索 dfs，岛屿数 count + 1 且在深度优先搜索中删除此岛屿。  
最终返回岛屿数 count 即可。  
## 二.数字中1的个数
### 1.[题目描述](https://leetcode-cn.com/problems/number-of-digit-one/submissions/)
给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。  
示例:  
输入: 13  
输出: 6   
解释: 数字 1 出现在以下数字中: 1, 10, 11, 12, 13 。  
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/LeetCode/数字1的个数/Solution.py)
这个题解题思路还是比较巧妙的，一句话说就是检查每个数位上的1的个数。[此处思路参考了牛客网](https://www.nowcoder.com/questionTerminal/bd7f978302044eee894445e244c7eee6)  
首先在0-10上，每个x属于\[0,9]不同的数字出现一次；在0-100上每个不同的数字出现10次；在0-1000上，每个不同的数字出现100次。  
设定变量res用来累加1的个数，x表示求取的什么位置上的1，q=n用来去判断当前处在那个位置。。  
只要q不为0就继续往下循环，首先设置digit=q%10，用来判断当前处于的这个数位上是整除还是余数为1还是余数大于1，这三种情况。  
设置q//=10，这个是对q除10取整数部分，也就是没有余数的部分，这部分1的个数为res += q*x，紧接着判断看如果digit大于1，则res += x,如果digit等于1，那么res += n%10 + 1，这里用n取余数是因为q在不断的变化中。到此完成一个循环，返回res值，即可。如果想不明白来千万注意写写画画。
