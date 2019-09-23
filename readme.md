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
## 三.[重建二叉树](https://www.nowcoder.com/practice/8a19cbe657394eeaac2f6ea9b0f6fcf6?tpId=13&tqId=11157&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
### 2.解题思路
二叉树的的题一般考虑递归的方法，递归包括三个部分，终止条件，裸机体，循环体。首先，前序遍历的方式是根左右，中序遍历的方式是左根右。所以前序遍历的第一个数一定是整个树的根结点，创建一个树的实例用来保存从前序遍历和中序遍历找到的数。知道根结点以后，在中序遍历里由根结点去划分左子树和右子树（没有重复的数，不用考虑根结点有重复数字的情况），中序遍历序列里这个值左边的就是左子树序列，右边的就是右子树序列。递归继续判断即可重建二叉树。需要注意，找到一个根结点以后要从前序遍历里删去这个结点。
## 四.[用两个栈实现对列](https://www.nowcoder.com/practice/54275ddae22f475981afa2244dd448c6?tpId=13&tqId=11158&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
### 2.解题思路
题目的要求就是用先进后出的方式去实现一个先进先出的功能。需要一个栈作为辅助栈。push的时候只要往主栈里压就可以了。pop的时候从主栈里把数按顺序放到辅助栈里，然后每次返回辅助栈的最上面的数就可以了。需要判断辅助栈有数的情况，主栈没数的情况，主栈有数辅助栈没数的情况。
## 五.[旋转数组的最小数字](https://www.nowcoder.com/practice/9f3231a991af4f55b95579b44b7a01ba?tpId=13&tqId=11159&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。  
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。  
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。  
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。  
### 2.解题思路
数组是一个非递减数组，也就是说可能是纯递增的，也有可能是递增的数组中，有重复的数。使用二分法，设定左右两个标，右边小于0说明数组为空直接返回0。如果左标志没有碰到右标志的时候遍历，先找到中间值，如果中间值大于等于右边界值，说明中间值位于前边的递增子数组里，则最小数一定在中间值右边，此时left=mid+1。如果中间值小于右边界值。说明中间值位于后边的递增子数组里，则证明最小数一定在中间值的左边,此时right等于mid.
## 六.[斐波那契数列](https://www.nowcoder.com/practice/c6c7742f5ba7442aada113136ddea0c3?tpId=13&tqId=11160&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。n<=39
### 2.解题思路
使用循环的思路，先设定初始数组为0和1，然后当数组小于n的时候，把这个数组最后两个数相加得到的那个数添加到这个初始数组里。最后返回这个初始数组的第n个数。
## 七.[二进制中1的个数](https://www.nowcoder.com/practice/8ee967e43c2c4ec193b040ea7fbb10b8?tpId=13&tqId=11164&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
## 1.题目描述
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
## 2.解题思路
按题目要求先判断输入的这个数是否是负数，如果是负数，则用他的补码去表示这个数。判断二进制数中1的个数，可以直接用自己与上自己减去1，如：1111&1110，答案是1110，然后1110&1101=1100，如此循环，这个数里有多少个1就能循环多少次，要使用一个标识位记录循环的次数。
# day4
今天继续总结题目思路。
## 一.[数值的整数次方](https://www.nowcoder.com/practice/1a834e5e3e1a4b7ba251417554e07c00?tpId=13&tqId=11165&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。  
保证base和exponent不同时为0  
### 2.解题思路
首先把exponent和base同时为0的情况判断掉，然后设定一个辅助变量value=1，如果exponent=0点时候，则直接返回value，循环exponent的绝对值次，每次循环都使value *= base，在循环外判断如果exponent小于0的话直接让value等于他的倒数。最后返回value即可
## 二.[调整数组顺序使奇数位于偶数的前边](https://www.nowcoder.com/practice/beb5aa231adc45b2a5dcc5b62c93f593?tpId=13&tqId=11166&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
### 2.解题思路
思路一: 设定两个数组，用来存放筛选遍历过的奇数和偶数。然后开始遍历数组，把奇数放在奇数的数组里，偶数放在偶数的数组里，遍历完成以后返回奇数数组和偶数数组的相加的列表即可。  
思路二(这个思路无法保证奇数和奇数偶数和偶数之间的相对位置不变)：设定两个指针，一个从前往后指一个从后往前指，保证第一个指针前面的数全是奇数，第二个指针后面的数全都是偶数。当第一个指针小于等于第二个指针的时候，指针开始移动，然后此时判断第一个指针指向的数是不是奇数，第二个指针指向的数是不是偶数。如果第一个指针指向的数不是奇数，跳出小循环，等待第二个指针指向的数不是偶数。交换两个位置上的数。在两个指针还没有相遇的时候交换这两个位置上的数。遍历完成以后就是前边是奇数序列，后边是偶数序列。
## 三.[链表中倒数第k个结点](https://www.nowcoder.com/practice/529d3ae5a407492994ad2a246518148a?tpId=13&tqId=11167&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
输入一个链表，输出该链表中倒数第k个结点。
### 2.解题思路
可以设定两个快慢指针，先让快指针走k步，然后再让快指针和慢指针一起走，当快指针走到最后指向空的时候，慢指针指向的位置就是倒数第k个结点。
## 四.[反转链表](https://www.nowcoder.com/practice/75e878df47f24fdc9dc3e400ec6058ca?tpId=13&tqId=11168&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
输入一个链表，反转链表后，输出新链表的表头。
### 2.解题思路
定义两个指针，分别记录当前位值和前一个位置。链表的反转需要把当前位置的结点指向前一个位置，最好设定一个中间变量，去存储cur.next，用来让cur指针可以继续往下走，因为当cur.next指向前一个位置以后，就和后面的位置断开了联系，要用一个中间变量去记录一下后边的位置。然后让中间变量指向下一个位置，当前指针指向前一个位置，前一个位置等于当前位置，当前位置等于中间变量。即可完成交换。
## 五.[合并两个排序的列表](https://www.nowcoder.com/practice/d8b6b4358f774294a89de2a6ac4d9337?tpId=13&tqId=11169&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
### 2.解题思路
思路1（递归）:首先设定两个变量head和temp，一个用来存储头结点的地址，一个用来遍历链表。采用递归的方法。终止条件有两个（同时用来做意外情况的判定）：链表1为空或者链表2为空。如果链表1为空的话，直接让temp.next=head2，如果链表2为空了，就把temp.next=head2。逻辑体：比较head1的值和head2的值看那个值小，就把temp.next指向这个链表，然后再把temp和temp.next链接起来,然后调用递归merge函数（参数要传入head1或head2的next），最终返回head.ext即可。需要注意的是递归是从最里层一层一层的返回，最外边返回的是第一个结点的值。  

思路2（非递归）：
首先设定两个变量head和temp，一个用来存储头结点的地址，一个用来遍历链表。head1和head2都有值的时候才遍历，如果head1的值小于head2的值，然后把temp.next指向head1,然后head1向后移动一位，否则指向head2，head2向后移动一位。进行完成后，temp再向后移动一位。如果head1为空了，则直接把剩下的head2的所有值符给temp.next。如果head2为空了，同理。最后返回，head.next即可。
# day 5
## 一.[树的子结构](https://www.nowcoder.com/practice/6e196c44c7004d15b1610b9afca8bd88?tpId=13&tqId=11170&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
### 1.题目描述
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
### 2.解题思路
主函数：设定一个标志位，做为判断是否找到子结构的返回结果，默认fasle。首先树不为空才进行判断，然后如果此时A,B中的值相等，则以这个值为根结点，传入判断函数（自写）看是否是其的一部分。如果此时两个值不相等的话，则再递归判断看左子树里是否有相等的值，然后在右子树里判断看是否有相等的值。最后返回设定的标志位result。  
判断函数：（递归），终止条件：如果第二棵树为空则证明已经判断完成，返回true，如果第一棵树遍历结束，或者第一课树和第二棵树的值不相等，返回false。
逻辑循环体：在不满足终止条件的情况下，就继续递归调用判断函数分别去判断看两棵树的左子树和右子树是否有包含。

