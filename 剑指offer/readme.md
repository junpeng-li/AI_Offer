# day1
正用python刷剑指offer，发现刷了近半，前边的东西遗忘较多，在老师的提醒下准备开始写总结。然后顺便记录一下自己秋招的历程吧。。加油！
先从今天刷的题开始写，然后以前刷的一点点补回来。

## 一.[树的子结构：](https://www.nowcoder.com/practice/6e196c44c7004d15b1610b9afca8bd88?tpId=13&tqId=11170&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking)
### 1.题目描述    
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）  
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/%E5%89%91%E6%8C%87offer/%E6%A0%91%E7%9A%84%E5%AD%90%E7%BB%93%E6%9E%84/Solution.py)  
解题的时候注意该画画图的就画下图吧。。  
主函数：  
1.首先看树1和树2的根结点是否一样，如果值一样，就以这个点为根结点判断树1是否包含树2 （送入判断函数）。   
2.如果值不一样，就在树1的左子树去找看是否有一样的点，如果没有，就再去树1的右子树找看是否有一样的点。    
3.如果遍历完了树2，说明树2是树1的子结构，如果遍历完了树1，说明树2不是树1的子结构。    
判断函数（递归）：  
终止条件：如果第二棵树为空则证明已经判断完成，返回true，如果第一棵树遍历结束，或者第一课树和第二棵树的值不相等，返回false。 逻辑循环体：在不满足终止条件的情况下，就继续递归调用判断函数分别去判断看两棵树的左子树和右子树是否有包含。

## 二.[顺时针打印矩阵](https://www.nowcoder.com/practice/9b4c81a02cd34f76be2659fa0d54342a?tpId=13&tqId=11172&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)

### 1.题目描述  
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.  
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/%E5%89%91%E6%8C%87offer/%E9%A1%BA%E6%97%B6%E9%92%88%E6%89%93%E5%8D%B0%E7%9F%A9%E9%98%B5/Solution.py)  
注意画图。
只需要一直取出矩阵的第一行，然后取出后再进行逆时针旋转90度就可以了。  
可以采用递归和非递归两种不同的解法。要注意矩阵的旋转方法。在非递归解法中采用了遍历的方法去形成新矩阵，遍历的时候应该注意行列之间的变换方法。在递归解法中使用了zip函数转置矩阵，然后用切片的方法使矩阵反向，达到逆时针旋转90度的目的。

# day2 
## 一.[包含min函数的栈](https://www.nowcoder.com/practice/4c776177d2c04c2494f2555c9fcc1e49?tpId=13&tqId=11173&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。  
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/%E5%89%91%E6%8C%87offer/%E5%8C%85%E5%90%ABmin%E5%87%BD%E6%95%B0%E7%9A%84%E6%A0%88/Solution.py)
这道题需要定义一个辅助栈，用来存储栈的最小值，因为这个辅助栈里的数是单调减小的，所以这个栈通常叫做单调栈。同时要设定一个min变量用来和新入栈的数做比较  
假设压入栈的数依次是:[3,5,2,6,1]  
则这个辅助栈里的数应该是:[3,3,2,2,1]  
入栈：如果新来一个数需要入栈，这个时候判断如果min为空或者传进来的数小于min，则把这个数同时压入主栈和单调栈。如果不是这样，则需要把min再压入单调栈一次，然后入栈的数进入主栈。  
出栈：出栈的时候需要同时把主栈和单调栈里的数弹出，但是只返回主栈的数  
查看栈顶元素和min函数就分别返回主栈和单调栈里的最后一个数就可以啦  

## 二.[栈的压入弹出序列](https://www.nowcoder.com/practice/d77d11405cc7470d82554cb392585106?tpId=13&tqId=11174&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）  
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/%E5%89%91%E6%8C%87offer/%E6%A0%88%E7%9A%84%E5%8E%8B%E5%85%A5%E5%BC%B9%E5%87%BA%E5%BA%8F%E5%88%97/Solution.py)
需要一个辅助栈，用来还原压栈顺序。把压入栈的次序依次遍历到辅助栈里，比较辅助栈的最后一个数是否和第二个序列的第一个数相等，如果和第二个序列的第一个数相等，则把这两个数弹出，第二个序列的位数往后移动一位（这里需要设定一个辅助变量j，用来移位，和判断是否完成遍历），如果遍历完成，辅助序列还不是空，则说明这个序列不是弹出序列。

# day3 
今天整理以前刷过的题的思路。
## 一.[二维数组中的查找](https://www.nowcoder.com/practice/abc3fe2ce8e146608e868a70efebf62e?tpId=13&tqId=11154&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。  
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/%E5%89%91%E6%8C%87offer/%E4%BA%8C%E7%BB%B4%E6%95%B0%E7%BB%84%E4%B8%AD%E7%9A%84%E6%9F%A5%E6%89%BE/Solution.py)
这个题首先要先确定数组大小长度不为空的时候往下走，从矩阵的右上角开始找，因为矩阵是从左到右递增，从上到下递增，如果矩阵的右上角那个数比target大，则所在的那一列就不用考虑了，列数减一，如果右上角那个数比target小，则这个数所在的这一行就不用考虑了，行数减一，循环。找到数就返回数，找不到就返回false。  

## 二.[替换空格](https://www.nowcoder.com/practice/4060ac7e3e404ad1a894ef3e17650423?tpId=13&tqId=11155&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/%E5%89%91%E6%8C%87offer/%E6%9B%BF%E6%8D%A2%E7%A9%BA%E6%A0%BC/Solution.py)
定义一个字符串变量。遍历传入的字符串，如果这个字符等于空格则把%20加到这个辅助字符串变量里，如果不是空格，就直接把当前这个字符加到字符串变量里，最后输出这个辅助字符串变量。
## 三.[重建二叉树](https://www.nowcoder.com/practice/8a19cbe657394eeaac2f6ea9b0f6fcf6?tpId=13&tqId=11157&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/剑指offer/重建二叉树/Solution.py)
二叉树的的题一般考虑递归的方法，递归包括三个部分，终止条件，裸机体，循环体。首先，前序遍历的方式是根左右，中序遍历的方式是左根右。所以前序遍历的第一个数一定是整个树的根结点，创建一个树的实例用来保存从前序遍历和中序遍历找到的数。知道根结点以后，在中序遍历里由根结点去划分左子树和右子树（没有重复的数，不用考虑根结点有重复数字的情况），中序遍历序列里这个值左边的就是左子树序列，右边的就是右子树序列。递归继续判断即可重建二叉树。需要注意，找到一个根结点以后要从前序遍历里删去这个结点。
## 四.[用两个栈实现对列](https://www.nowcoder.com/practice/54275ddae22f475981afa2244dd448c6?tpId=13&tqId=11158&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/剑指offer/用两个栈实现队列/Solution.py)
题目的要求就是用先进后出的方式去实现一个先进先出的功能。需要一个栈作为辅助栈。push的时候只要往主栈里压就可以了。pop的时候从主栈里把数按顺序放到辅助栈里，然后每次返回辅助栈的最上面的数就可以了。需要判断辅助栈有数的情况，主栈没数的情况，主栈有数辅助栈没数的情况。
## 五.[旋转数组的最小值](https://www.nowcoder.com/practice/9f3231a991af4f55b95579b44b7a01ba?tpId=13&tqId=11159&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。  
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。  
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。  
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。  
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/剑指offer/旋转数组的最小值/Solution.py)
数组是一个非递减数组，也就是说可能是纯递增的，也有可能是递增的数组中，有重复的数。使用二分法，设定左右两个标，右边小于0说明数组为空直接返回0。如果左标志没有碰到右标志的时候遍历，先找到中间值，如果中间值大于等于右边界值，说明中间值位于前边的递增子数组里，则最小数一定在中间值右边，此时left=mid+1。如果中间值小于右边界值。说明中间值位于后边的递增子数组里，则证明最小数一定在中间值的左边,此时right等于mid.
## 六.[斐波那契数列](https://www.nowcoder.com/practice/c6c7742f5ba7442aada113136ddea0c3?tpId=13&tqId=11160&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。n<=39
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/剑指offer/斐波那契数列/Solution.py)
使用循环的思路，先设定初始数组为0和1，然后当数组小于n的时候，把这个数组最后两个数相加得到的那个数添加到这个初始数组里。最后返回这个初始数组的第n个数。
## 七.[二进制中1的个数](https://www.nowcoder.com/practice/8ee967e43c2c4ec193b040ea7fbb10b8?tpId=13&tqId=11164&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
## 1.题目描述
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
## 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/剑指offer/二进制中1的个数/Solution.py)
按题目要求先判断输入的这个数是否是负数，如果是负数，则用他的补码去表示这个数。判断二进制数中1的个数，可以直接用自己与上自己减去1，如：1111&1110，答案是1110，然后1110&1101=1100，如此循环，这个数里有多少个1就能循环多少次，要使用一个标识位记录循环的次数。
# day4
今天继续总结题目思路。
## 一.[数值的整数次方](https://www.nowcoder.com/practice/1a834e5e3e1a4b7ba251417554e07c00?tpId=13&tqId=11165&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。  
保证base和exponent不同时为0  
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/剑指offer/数值的整数次方/Solution.py)
首先把exponent和base同时为0的情况判断掉，然后设定一个辅助变量value=1，如果exponent=0点时候，则直接返回value，循环exponent的绝对值次，每次循环都使value *= base，在循环外判断如果exponent小于0的话直接让value等于他的倒数。最后返回value即可
## 二.[调整数组顺序使奇数位于偶数的前边](https://www.nowcoder.com/practice/beb5aa231adc45b2a5dcc5b62c93f593?tpId=13&tqId=11166&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/剑指offer/调整数组顺序使奇数位于偶数的前边/Solution.py)
思路一: 设定两个数组，用来存放筛选遍历过的奇数和偶数。然后开始遍历数组，把奇数放在奇数的数组里，偶数放在偶数的数组里，遍历完成以后返回奇数数组和偶数数组的相加的列表即可。  
思路二(这个思路无法保证奇数和奇数偶数和偶数之间的相对位置不变)：设定两个指针，一个从前往后指一个从后往前指，保证第一个指针前面的数全是奇数，第二个指针后面的数全都是偶数。当第一个指针小于等于第二个指针的时候，指针开始移动，然后此时判断第一个指针指向的数是不是奇数，第二个指针指向的数是不是偶数。如果第一个指针指向的数不是奇数，跳出小循环，等待第二个指针指向的数不是偶数。交换两个位置上的数。在两个指针还没有相遇的时候交换这两个位置上的数。遍历完成以后就是前边是奇数序列，后边是偶数序列。
## 三.[链表中倒数第k个结点](https://www.nowcoder.com/practice/529d3ae5a407492994ad2a246518148a?tpId=13&tqId=11167&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
输入一个链表，输出该链表中倒数第k个结点。
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/剑指offer/链表中倒数第k个结点/Solution.py)
可以设定两个快慢指针，先让快指针走k步，然后再让快指针和慢指针一起走，当快指针走到最后指向空的时候，慢指针指向的位置就是倒数第k个结点。
## 四.[链表反转](https://www.nowcoder.com/practice/75e878df47f24fdc9dc3e400ec6058ca?tpId=13&tqId=11168&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
输入一个链表，反转链表后，输出新链表的表头。
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/剑指offer/链表反转/Solution.py)
定义两个指针，分别记录当前位值和前一个位置。链表的反转需要把当前位置的结点指向前一个位置，最好设定一个中间变量，去存储cur.next，用来让cur指针可以继续往下走，因为当cur.next指向前一个位置以后，就和后面的位置断开了联系，要用一个中间变量去记录一下后边的位置。然后让中间变量指向下一个位置，当前指针指向前一个位置，前一个位置等于当前位置，当前位置等于中间变量。即可完成交换。
## 五.[合并两个排序的链表](https://www.nowcoder.com/practice/d8b6b4358f774294a89de2a6ac4d9337?tpId=13&tqId=11169&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
### 2.解题思路
[思路1（递归）](https://github.com/junpeng-li/AI_Offer/blob/master/剑指offer/合并两个排序的链表/Selation1.py): 
首先设定两个变量head和temp，一个用来存储头结点的地址，一个用来遍历链表。采用递归的方法。终止条件有两个（同时用来做意外情况的判定）：链表1为空或者链表2为空。如果链表1为空的话，直接让temp.next=head2，如果链表2为空了，就把temp.next=head2。逻辑体：比较head1的值和head2的值看那个值小，就把temp.next指向这个链表，然后再把temp和temp.next链接起来,然后调用递归merge函数（参数要传入head1或head2的next），最终返回head.ext即可。需要注意的是递归是从最里层一层一层的返回，最外边返回的是第一个结点的值。  

[思路2（非递归）](https://github.com/junpeng-li/AI_Offer/blob/master/剑指offer/合并两个排序的链表/Solution2.py)：
首先设定两个变量head和temp，一个用来存储头结点的地址，一个用来遍历链表。head1和head2都有值的时候才遍历，如果head1的值小于head2的值，然后把temp.next指向head1,然后head1向后移动一位，否则指向head2，head2向后移动一位。进行完成后，temp再向后移动一位。如果head1为空了，则直接把剩下的head2的所有值符给temp.next。如果head2为空了，同理。最后返回，head.next即可。
# day 5
## 一.[二叉树的镜像](https://www.nowcoder.com/practice/564f4c26aa584921bc75623e48ca3011?tpId=13&tqId=11171&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
把二叉树变为他的镜像。
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/剑指offer/二叉树的镜像/Solution.py)
把原来的二叉树变为他的镜像，即左结点变为右结点，右结点变为左结点。  
采用递归的思路，终止条件：树遍历结束。逻辑体：左结点值和右结点值交换(设定中间值遍量，或者python中可以一行解决)。循环体：先递归左子树，再递归右子树。
## 二.[数组中重复的数字](https://www.nowcoder.com/practice/623a5ac0ea5b4e5f95552655361ae0a8?tpId=13&tqId=11203&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。  
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/剑指offer/数组中重复的数字/Solution.py)
因为题目是在0到n-1点范围内。所以可以利用现有的数作标志，如果遍历过了这个数，则在数组里以这个数为下标的位置上加上n。之后再遇到相同值的时候会发现，这个值对应下标位置是大于n的，此时这个数字就是重复数字。在判断这个值对应下标位置的数是否大于n之前需要加上一条过滤条件。因为有可能会出现没有遍历过这个位置的数，但是这个位置的数已经被加过n了的情况，所以需要判断看这个位置的数是否大于n，如果大于n，则直接减n让他在作为index的值恢复原来的数。这里并没有改变数组，仅仅只是改变了循环查找时的下标。
## 三.[正则表达式匹配](https://www.nowcoder.com/practice/45327ae22b7b413ea21df13ee7d6429c?tpId=13&tqId=11205&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/剑指offer/正则表达式匹配/Solution.py)
这个题主要考察思维的缜密性。有四大种情况需要判断。  
1.如果s和pattern都为空，则返回true。  
2.如果s不为空pattern为空，返回false。  
3.如果s为空pattern不为空，则进一步判断看pattern长度是否大于1而且第二个字符是不是*，如果是*则前方两个字符等于不存在，继续递归调用match函数传入s和pattern[2:]进行后边的判断。如果pattern长度没有大于0或者第二个字符不是*，返回false。  
4，如果s和pattern都不为空则需进行更进一步的判断：  
此时再细分两种情况：  
(1)判断如果s的长度大于1并且pattern的第二个字符是*。则继续嵌套判断，如果s[0]不等于pattern[0]并且pattern的第一个字符不是.，此时相当于pattern前两个字符不起作用，递归调用s和pattern[2:]，从pattern的第三个字符开始匹配。如果不是这种状况（即pattern[0]与s[0]相等，或者pattern[0]为.，且此时pattern的第二个字符是*），此时则前两个字符起了作用，此时pattern的前两个字符是.*,在正则中点星点意义是可以匹配0到多个字符，则可以把s不变，pattern向后移动两位，此时相当于把pattern的前两个字符看成了没有；也可以把s向后移动一位，pattern移动两位，相当于pattern两个字符匹配了s的一位字符；也可以把s向后移动一位，pattern不变，此时相当于pattern匹配s的多个位置。  
(2)如果不是第一种状况（即s的长度小于等于1或者pattern第二个字符不是*）。此时则需要嵌套判断看s和pattern的第一个字符是不是相等，或者看pattern的第一个字符是不是.，如果是就继续递归,s和pattern往后移动一位判断。如果不是则返回false。
# day6
# 一.[表示数值的字符串](https://www.nowcoder.com/practice/6f8c901d091949a5837e24bb82a731f2?tpId=13&tqId=11206&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/剑指offer/表示数值的字符串/Solution.py)
从头开始遍历字符串，判断是否为数值需要判断的大情况分为四种。分别是e，符号，小数点，看每位数是否在0-9范围内。由于前三种情况可能会存在关联判断的情况(如：小数点前不能出现小数点和e)，所以需要设定三个标志位，用来标志看这三种情况是否已经出现过了。   
(1)对于e来说，e不能出现两次，也不能出现在最后，因为e后面要有数字。需要判断e是不是第二次出现，还要判断e的位置是不是最后一个。  
(2)对于符号位来说。如果符号位第一次出现,若不是在首位出现，则只能出现在e的后面。如果符号第二次出现，则只能出现在e后面。所以如果符号是第二次出现，则看是不是跟在e之后，如果不是返回false。如果如果符号第一次出现，把符号相关标志位记为true，若在这种情况下i>0,且符号前一个字符不是e，则返回false。  
(3)对于小数点来说。小数点不能出现两次，小数点前不能出现e。即小数点前不能有小数点和e。  
(4)对于其余都状况来说，如果每个字符小于0，大于9，则返回false。  
如果都没有满足上述的条件，直接返回true。  
## 二.[链表中环的入口结点](https://www.nowcoder.com/practice/253d2c59ec3e4bc68da16833f79a38e4?tpId=13&tqId=11208&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/剑指offer/链表中环的入口结点/Solution.py)
首先利用快慢指针的方法，判断看这个里有没有环，即先设定两个指针指向头结点，一个判断有无指针的标志位，快指针每次走两步，慢指针每次走一步，如果两个指针相遇，则说明有环。如果有环的话需要设定一个slow2指针让其从头开始走，另一个指针从快慢指针相遇的那个位置开始走，当slow2和另一个指针相遇的点，就是环的入口处。（此处证明可以自己画图思考一下，或者从网上搜一下证明）。  
# day7
## 一.[删除链表中重复的结点](https://www.nowcoder.com/practice/fc533c45b73a41b0b44ccba763f866ef?tpId=13&tqId=11209&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/剑指offer/删除链表中重复的结点/Solution.py)
删除重复结点，遍历链表，然后一个个把非重复指针串联起来就可以了。  
终止条件：如果head或head.next为空则停止递归，返回head。  
循环逻辑体：比较看当前结点的值和next指针的值是不是相等，如果相等的话，设定一个辅助指针p为head.next.next，让p往后走直到p为空或者p的值不等于当前结点的值，递归返回继续处理以p为头结点的情况。如果当前结点的值和下个结点的值不相等，则以继续递归处理以下个结点为头结点的情况，最终返回头结点即可。
## 二.[二叉树的下一个结点](https://www.nowcoder.com/practice/9023a0c988684a53960365b889ceaf5e?tpId=13&tqId=11210&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/剑指offer/二叉树的下一个结点/Solution.py)
中序遍历的顺序是左根右。找树的下一个结点的话，需要判断看这个树是有没有右子树。首先判断给定结点是否有右子树，这个结点有右子树，则直接返回右子树的最左边那个数即可。如果给定结点没有右子树，则需要看这个结点的下一个值的左结点是不是这个结点，如果是，则返回这个结点的下一个结点即可。其他情况为none
# day8
## 一.[对称的二叉树](https://www.nowcoder.com/practice/ff05d44dfdb04e1d83bdbdab320efbcb?tpId=13&tqId=11211&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/剑指offer/对称的二叉树/Solution.py)
一个二叉树是不是对称的就是看左右树是否对称。即把这一棵树的左子树和右子树看成两棵树，看树1的左子树是不是等于树2点右子树，树2点右子树是不是等于树1点左子树。  
主函数：  
先判断树是不是空，如果是空直接返回true。如果不是空，把分别把树的左子树和右子树作为参数传入一个判断函数。返回这个判断函数的值即可。  
判断函数（递归）：  
终止条件：如果两棵树其中有一棵为空，则只有两棵树都为空才会返回true。如果两棵树值不同，直接返回false。  
循环逻辑体：递归返回，看树1的左子树是不是等与树2的右子树，树1点右子树是不是等于树2点左子树。

## 二.[矩阵中的路径](https://www.nowcoder.com/practice/c61c6999eecb4b8f88a98f66b273a3cc?tpId=13&tqId=11218&tPage=4&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。 例如 a b c e s f c s a d e e 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/剑指offer/矩阵中的路径/Solution.py)
整体思路就是在matrix里找与path字符相同格子，以这个格子为起点，去查找上下左右的数，看是否有和path里相同的，如果有就继续往前走，如果没有就返回上一步，继续寻找在matrix里与path第一个字符相同的格子，若遍历完成还没找到就返回false。   
具体步骤：  
主函数：  
先排除异常：若matrix为空，则直接返回false。如果path为空则返回true。  
把matrix根据给定的行列数，把列表转换成矩阵。然后循序遍历矩阵，把矩阵，i，j，path分别传入判断函数，若为true则存在。  
判断函数：
每次取path字符串的第一个数与matrix[i][j]进行比较，看是否相同，如果相同，则在这个字母周围寻找其他符号条件的字母。  
递归终止条件：如果找到匹配的就继续判断path的下一个字母，直到p为空，则证明存在该路径。遍历的时候注意一点，把每个遍历过的matrix[i][j]变成空格。这一轮遍历完成过后如果没有找到相同的，则恢复的到原来的数值继续往下判断。  
递归循环逻辑体：递归循环的时候需要根据矩阵的边界设定条件，利用i,j的活动把matrix，上下左右，需要比对的path下一个字母，传入判断函数进行判断看是否相等。如果有返回true，如果全部都不满足，则返回false。  
要是第一个字符就不相等直接返回false。
## 三.[机器人的运动路径](https://www.nowcoder.com/practice/6e5207314b5241fb83f2329e89fdecc8?tpId=13&tqId=11219&tPage=4&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/剑指offer/机器人的运动路径/Solution.py)
初始化一个集合，用来存放走过的格子，把k值和起始点0，0传入搜索函数，让机器人走。最终检查集合的长度就是机器人走过的长度。  
判断函数：  
用来判断看机器人走过的路线加和是否超过了k值。利用map函数吧这些数变成整形，然后i相加，j相加。 返回加和是否小于k值。  
搜索函数：  
递归终止条件：如果ij加和超过k值或者ij在集合里，停止遍历。  
循环逻辑体：  
把未走过的ij加到集合里。从左上角开始一直往右和下递归循环遍历搜索函数即可，可以确保每个格子都能被检索到。即只要i没有超出行数就i+1往下找，j没有超出列就j+1往右找。
## 四.[剪绳子](https://www.nowcoder.com/practice/57d85990ba5b440ab888fc72b0751bf8?tpId=13&tqId=33257&tPage=4&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
给你一根长度为n的绳子，请把绳子剪成m段（m、n都是整数，n>1并且m>1），每段绳子的长度记为k[0],k[1],...,k[m]。请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/剑指offer/剪绳子/Solution.py)
证明摘自牛客网题解（qt菜鸡弟弟）。   
贪婪解法：当n大于等于5时，我们尽可能多的剪长度为3的绳子；当剩下的绳子长度为4时，把绳子剪成两段长度为2的绳子。 为什么选2，3为最小的子问题？因为2，3包含于各个问题中，如果再往下剪得话，乘积就会变小。 为什么选长度为3？因为当n≥5时，3(n−3)≥2(n−2)。
具体步骤：  
贪婪法，尽可能选择更多的3。如果number长度小于3，则直接返回这个数。设定辅助变量val=1用来存储乘积，如果number%3==1，则val*=4，然后减去4(余数为1，若减1则最后的val只能乘3，减4可以乘4),如果number%3==2，则val*=2,然后减去2。这样可以保证经过过滤后的number一定可以被3整除。遍历number，每次val*=3，number减3，直到number为0。
# day9
## 一.[从上倒下打印二叉树](https://www.nowcoder.com/practice/7fe2212963db4790b57431d9ed259701?tpId=13&tqId=11175&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/剑指offer/从上到下打印二叉树/Solution.py)
设定一个辅助队列存入头结点，用来遍历树；一个辅助数组用来存放结果。只要队列里还有数，就遍历。每次取辅助队列里的第一个数，把它的值传入到结果队列里，然后判断看这个结点有没有左子树或者右子树,如果有，则把这个树的左子树或右子树放入队列的后面继续遍历，队列为空的时候即为遍历完成
## 二.[分行从上到下打印二叉树](https://www.acwing.com/problem/content/42/)
### 1.题目描述
从上到下按层打印二叉树，同一层的结点按从左到右的顺序打印，每一层打印到一行。
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/剑指offer/分行从上到下打印二叉树/Solution.py)
分行打印需要每行分开，于是相较于不分行打印，就需要多设定一个辅助数组，用来存放每一行里的数据，一个用来计算当前层结点个数的辅助变量，一个用来计算下一层结点个数的辅助变量。
具体思路：
分行需要设定两个辅助变量，记录当前这一层需要打印的结点数，以及下一层需要打印的结点数,设定一个辅助队列，用来遍历结点；一个当前层结果数组，存储当前这一层需要存储的结果；一个结果数组用来存储最终结果,把头结点添加到队列以后，开始遍历队列，每次弹出队列里的第一个元素，把这个值添加到当前结果数组里，当前个数减一,然后看以这个结点为头结点有没有左右子树，如果有的话，把他们放入queue里，并且下一层个数加一,如果当前个数为0了，说明这一层已经打印完毕，然后把当前层结果添加到总结果里，下一层个数复制给当前层个数,下一层个数清0，当前层结果变为空。
## 三.[之字形打印二叉树](https://www.nowcoder.com/practice/91b69814117f4e8097390d107d2efbe0?tpId=13&tqId=11212&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/剑指offer/之字形从上到下打印二叉树/Solution.py)
相较于分行打印二叉树，这个题目只需要增加一个判断奇偶行的辅助变量，然后在最后把当前层的数按奇偶行反转或不反转即可。
# day 10
## 一.[二叉树中和为某一值的路径](https://www.nowcoder.com/practice/b736e784e3e34731af99065031301bca?tpId=13&tqId=11177&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)
## 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/剑指offer/二叉树中和为某一值的路径/Solution.py)
这个题是要求二叉树路径的和是否等于给定的数。即遍历二叉树的同时记录路径，把这条路径上的每一个值相加看是否等于target(可以采用减法的形式，判断这个路径的值减到最后是不是0)，输出所有满足这个条件的路径。采用递归的方法去遍历这个二叉树。  
具体步骤：  
设定两个数组，一个用来存放最后的结果，一个用来存放这条路径。首先判断这个树是否是空，如果是空直接返回空列表。把这个结点的值放到path数组里，然后target减去这个结点的值。  
递归终止条件：在这个结点没有左右子树（即结点为叶子结点）并且target为0时，把记录当前路径的path数组加到answer数组里（此处需要注意，要把path的值赋给answer，否则answer会跟着path变）。  
循环逻辑体：递归处理左右子树。  
处理完最后要从path里把这个数pop掉，用来存放下一个结果。最终在最外层返回answer即可。

## 二.[二叉搜索树的后序遍历](https://www.nowcoder.com/practice/a861533d45854474ac791d90e447bafd?tpId=13&tqId=11176&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/%E5%89%91%E6%8C%87offer/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%90%8E%E5%BA%8F%E9%81%8D%E5%8E%86/Soluthon.py)
后序遍历的顺序是左右根，二叉搜索树里所有的左子树要比跟结点大，所有的右子树要比根结点小。  
首先后序遍历的特点找到跟结点（取最后一个数），然后根据找到的根结点带回原序列遍历去比较，然后找到左右子树，这个数之前的为左子树，数之后是右子树。（如果找到第一个比根结点大的数后面还有比这个数大的直接返回false）。设置两个辅助变量，left和right，用来作为标志位去判断是否是二叉搜索树的最后结果。递归判断左右子树，利用切片的方式从原数列中找到左子树序列和右子树序列传入函数进行递归，当i>0的时候判断左子树，i<length-1的时候判断右子树。  
当left和right都为true的时候证明这个树是二叉搜索树的后序遍历结果。
# day 11
## 一.[复杂链表的复制](https://www.nowcoder.com/practice/f836b2c43afc4b35ad6adc41ec941dba?tpId=13&tqId=11178&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/剑指offer/复杂链表的复制/Solution.py)
1.把原链表的每个结点复制一下。  
2.遍历处理随机指针，如果原链表有随机指针的话，那么复制链表的随机指针即为原链表随机指针的下一个位置。  
3.把原链表和复制链表分开。  
具体做法：  
1.复制结点：设定一个辅助变量dummy去记录当前位置的头结点位置，然后开始遍历，把每一个复制结点放在原链表对应结点的后面。最后让dummy向下移动一个位置。  
2.处理随机指针：dummy=head，继续从原头结点开始遍历，设定一个变量标记dummy.next为copynode。查找每一个原结点是否存在随机指针，如果存在随机指针，则copynode的随机指针即为原链表结点指针的下一个位置。因为此时两个原结点中间有一个复制结点，所以最后需要让dummy=copynode.next，向后移动两个位置进行遍历。  
3.把原链表和复制链表分开。设定两个辅助变量，一个用来标记原链表头结点，一个用来标记复制链表的头结点。只要原链表结点存在就继续遍历，设定一个变量copeNode=dummy.next用来标记那些是复制结点,如果原链表结点的下一个结点存在的话，则copyNode.next=dummynext.next，如果不存在则把copyNode.next指向None.最后返回复制链表的头结点即可。
#day 18
状态不太好。。。晕晕乎乎继续开始
## 一.[数组中出现次数超过一半的数字](https://www.nowcoder.com/practice/e8a1b01a2df14cb2b228b30ee6a92163?tpId=13&tqId=11181&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/%E5%89%91%E6%8C%87offer/%E6%95%B0%E7%BB%84%E4%B8%AD%E5%87%BA%E7%8E%B0%E6%AC%A1%E6%95%B0%E8%B6%85%E8%BF%87%E4%B8%80%E5%8D%8A%E7%9A%84%E6%95%B0%E5%AD%97/Solution.py)
思路1，可以对数组进行排序，然后针对排序过后对数组，取出中间对那个数字，必定是出现次数超过数组长度一半的。  
思路2，设置一个辅助变量计算数字出现的从次数，一个辅助变量保存当前这个数。从第一个数开始遍历，如果后面的这个数和第一个数相同，则次数变量加一，如果不同次数变量减一。若次数变量为0的时候，储存数字的变量减一换成后面的这个数，然后把次数变量置1。遍历结束，最终保存在辅助数组里的那个数就是要求的数，再判断一下这个数是不是在数组中出现的次数满足要求即可。
## 二.[序列化二叉树](https://www.nowcoder.com/practice/cf7e25aa97c04cc1a68c8f040e71fb84?tpId=13&tqId=11214&tPage=4&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
请实现两个函数，分别用来序列化和反序列化二叉树  
二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，从而使得内存中建立起来的二叉树可以持久保存。序列化可以基于先序、中序、后序、层序的二叉树遍历方式来进行修改，序列化的结果是一个字符串，序列化时通过 某种符号表示空节点（#），以 ！ 表示一个结点值的结束（value!）。  
二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。  
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/%E5%89%91%E6%8C%87offer/%E5%BA%8F%E5%88%97%E5%8C%96%E4%BA%8C%E5%8F%89%E6%A0%91/Solution.py)
序列化：用前序遍历的方法遍历整棵树，按要求把树里的数值，排列成一个序列。  
反序列化：先把字符串转换为列表的格式，然后针对这个列表，用前序遍历的思路把树建起来即可。
## 三.[二叉搜索树的后序遍历序列](https://www.nowcoder.com/practice/a861533d45854474ac791d90e447bafd?tpId=13&tqId=11176&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/%E5%89%91%E6%8C%87offer/%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E5%90%8E%E5%BA%8F%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97/Solution.py)
后序遍历是左右根，二叉搜索树里的所有左子树要比根结点小，右子树要比根结点大，可以先通过后序遍历的最后一个数确定这棵树的根结点，然后用递归分别判断前后两个部分是否符合要求。
## 四.[字符串的排列](https://github.com/junpeng-li/AI_Offer/blob/master/%E5%89%91%E6%8C%87offer/%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9A%84%E6%8E%92%E5%88%97/Solution.py)
### 1.题目描述
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/剑指offer/字符串的排列/Solution.py)
如果字符串少于1个则直接返回这个字符串即可。设定一个结果列表存储最终的结果，循环遍历，每次固定一个字符i，嵌套循环j，然后其他的字符利用切片的方法把数组传进去进行递归循环。最后判断如果结果数组里没有这个组合，就把这个组合j添加到结果数组里。
## 五.[最小的k个数](https://www.nowcoder.com/practice/6a296eb82cf844ca8539b57c23e6e9bf?tpId=13&tqId=11182&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/剑指offer/最小的k个数/Solution.py)
写一个快排，然后把输入的序列用快排排好，取前k个数即可。
# day 19 
我真是个菜鸡，放平心态，该干啥干啥。
## 一.[从尾到头打印链表](https://www.nowcoder.com/practice/d0267f7f55b3412ba93bd35cfa8e8035?tpId=13&tqId=11156&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
### 2.[解题思路](https://github.com/junpeng-li/AI_Offer/blob/master/剑指offer/从尾到头打印链表/Solution.py)
从尾到头打印链表，自然就想到了可以使用辅助栈去打印这个链表。所以可以先设定一个列表作为辅助栈，如果链表不为空的话，就把当前节点的值取出来，放到这个栈里，然后将节点向下移动，最后将辅助栈反转输出，则返回的就是从尾到头的链表的值。
