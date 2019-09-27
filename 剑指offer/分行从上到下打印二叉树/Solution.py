# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printFromTopToBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #分行需要设定两个辅助变量，记录当前这一层需要打印的结点数，以及下一层需要打印的结点数
        #设定一个辅助队列，用来遍历结点；一个当前层结果数组，存储当前这一层需要存储的结果；
        #一个结果数组用来存储最终结果
        #把头结点添加到队列以后，开始遍历队列，每次弹出队列里的第一个元素，把这个值添加到当前结果数组里，当前个数减一
        #然后看以这个结点为头结点有没有左右子树，如果有的话，把他们放入queue里，并且下一层个数加一
        #如果当前个数为0了，说明这一层已经打印完毕，然后把当前层结果添加到总结果里，下一层个数复制给当前层个数
        #下一层个数清0，当前层结果变为空
        if not root:
            return []
        result = []
        cur_result = []
        queue = [root]
        cur_number = 1
        next_number = 0
        while len(queue) > 0:
            node = queue.pop(0)
            cur_result.append(node.val)
            cur_number -= 1
            if node.left:
                queue.append(node.left)
                next_number += 1
            if node.right:
                queue.append(node.right)
                next_number += 1
            if cur_number == 0:
                result.append(cur_result)
                cur_number = next_number
                next_number = 0
                cur_result = []
        return result



