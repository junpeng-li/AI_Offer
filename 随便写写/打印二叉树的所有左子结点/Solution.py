class Solution(object):
    def printLeftNode(self,root):
        if not hasatrr(self,'res'):
            self.res = []
        if root:
            if root.left:
                self.res.append(root.left.val)
                self.printLeftNode(root.left)
            if root.right:
                self.printLeftNode(root.right)
       return self.res
