# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
class Solution:
    n = 1
    def help(self, p, q):
        if p == None and q == None: return n
        if p or q :
            n += 1
            return self.help(p.right, p.left) and self.help(q.left, q.right)

    def maxDepth(self, root: TreeNode) -> int:
        if root:
            return self.help(root.left, root.right)
            """

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0      
        depth_l = self.maxDepth(root.left)
        depth_r = self.maxDepth(root.right)
        #print depth_l,depth_r 
        if depth_l > depth_r :
            return depth_l + 1
        else:
            return depth_r + 1
