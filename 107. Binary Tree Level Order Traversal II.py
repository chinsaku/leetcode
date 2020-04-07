# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def help(self, p, q):
        if p == None and q == None: return True
        if p and q and p.val == q.val:
            return self.help(p.right, q.left) and self.help(p.left, q.right)
        return False
        
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
       if root  == None:
           return [[root.val]]
        depth_l = self.levelOrderBottom(root.left)
        depth_r = self.levelOrderBottom(root.right)
            #print depth_l,depth_r 
        if depth_l > depth_r :
            return depth_l + 1
        else:
            return depth_r + 1
