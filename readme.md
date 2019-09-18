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

