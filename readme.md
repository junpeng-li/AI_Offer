# day1
正刷剑指offer，发现刷了近半，前边的东西遗忘较多，在老师的提醒下准备开始写总结。然后顺便记录一下自己秋招的历程吧。。加油！
先从今天刷的题开始写，然后以前刷的一点点补回来。  

## 一.[树的子结构：](https://www.nowcoder.com/practice/6e196c44c7004d15b1610b9afca8bd88?tpId=13&tqId=11170&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking)
### 1.题目描述    
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）  
### 2.解题思路  
解题的时候注意该画画图的就画下图吧。。  
1.首先判断树1和树2的根结点是否一样，如果值一样，就以这个点为根结点判断树1是否包含树2  
2.如果值不一样，就在树1的左子树去找看是否有一样的点，如果没有，就再去树1的右子树找看是否有一样的点。  
3.如果遍历完了树2，说明树2是树1的子结构，如果遍历完了树1，说明树2不是树1的子结构。  

## 二.[顺时针打印矩阵](https://www.nowcoder.com/practice/9b4c81a02cd34f76be2659fa0d54342a?tpId=13&tqId=11172&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)

### 1.题目描述  
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.  
### 2.解题思路  
注意画图。
只需要一直取出矩阵的第一行，然后取出后再进行逆时针旋转90度就可以了。  
可以采用递归和非递归两种不同的解法。要注意矩阵的旋转方法。在非递归解法中采用了遍历的方法去形成新矩阵，遍历的时候应该注意行列之间的变换方法。在递归解法中使用了zip函数转置矩阵，然后用切片的方法使矩阵反向，达到逆时针旋转90度的目的。

# day2 
## 一.[包含min函数的栈](https://www.nowcoder.com/practice/4c776177d2c04c2494f2555c9fcc1e49?tpId=13&tqId=11173&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。  
### 2.解题思路
这道题需要定义一个辅助栈，用来存储栈的最小值，因为这个辅助栈里的数是单调减小的，所以这个栈通常叫做单调栈。同时要设定一个min变量用来和新入栈的数做比较  
假设压入栈的数依次是:[3,5,2,6,1]  
则这个辅助栈里的数应该是:[3,3,2,2,1]  
入栈：如果新来一个数需要入栈，这个时候判断如果min为空或者传进来的数小于min，则把这个数同时压入主栈和单调栈。如果不是这样，则需要把min再压入单调栈一次，然后入栈的数进入主栈。  
出栈：出栈的时候需要同时把主栈和单调栈里的数弹出，但是只返回主栈的数  
查看栈顶元素和min函数就分别返回主栈和单调栈里的最后一个数就可以啦  

## 二.[栈的压入弹出序列](https://www.nowcoder.com/practice/d77d11405cc7470d82554cb392585106?tpId=13&tqId=11174&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）  
### 2.解题思路
需要一个辅助栈，用来还原压栈顺序。把压入栈的次序依次遍历到辅助栈里，比较辅助栈的最后一个数是否和第二个序列的第一个数相等，如果和第二个序列的第一个数相等，则把这两个数弹出，第二个序列的位数往后移动一位（这里需要设定一个辅助变量j，用来移位，和判断是否完成遍历），如果遍历完成，辅助序列还不是空，则说明这个序列不是弹出序列。

# day3 
今天整理以前刷过的题的思路。
## 一.[二维数组中的查找](https://www.nowcoder.com/practice/abc3fe2ce8e146608e868a70efebf62e?tpId=13&tqId=11154&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。  
### 2.解题思路
这个题首先要先确定数组大小长度不为空的时候往下走，从矩阵的右上角开始找，因为矩阵是从左到右递增，从上到下递增，如果矩阵的右上角那个数比target大，则所在的那一列就不用考虑了，列数减一，如果右上角那个数比target小，则这个数所在的这一行就不用考虑了，行数减一，循环。找到数就返回数，找不到就返回false。  

## 二.[替换空格](https://www.nowcoder.com/practice/4060ac7e3e404ad1a894ef3e17650423?tpId=13&tqId=11155&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
### 2.解题思路
定义一个字符串变量。遍历传入的字符串，如果这个字符等于空格则把%20加到这个辅助字符串变量里，如果不是空格，就直接把当前这个字符加到字符串变量里，最后输出这个辅助字符串变量。
