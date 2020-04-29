# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sum_def(self,root):
        if root == None:
            return [0]
        if root.left == None:
            return [root.val+ i for i in self.sum_def(root.right)]
        if root.right == None:
            return [root.val + i for i in self.sum_def(root.left)]
        b = [root.val + i  for i in self.sum_def(root.left)]
        a = [root.val + i  for i in self.sum_def(root.right)]
        return a+b


    def hasPathSum(self, root, sum):
        if root ==None:
            return True
        for i in self.sum_def(root):
            if sum == i:
                return True
        return False

a =TreeNode(1)
b =TreeNode(2)
c =TreeNode(3)
c.left=a
c.right=b
d =None
#m =Solution().hasPathSum(d,0)
n =Solution().sum_def(d)

print(n)