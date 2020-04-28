# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
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
"""

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        queue = [(root, 0)]
        while len(queue) > 0:
            node, depth = queue.pop()
            if node:
                print('node.val=',node.val)
                if len(res) <= depth:
                    res.insert(0, [])
                    print('res=',res)
                res[-(depth+1)].append(node.val)
                print('res2=',res)
                queue.insert(0, (node.left, depth+1))
                queue.insert(0, (node.right, depth+1))
                print('queue=',queue)
        return res

a=TreeNode(15)
b=TreeNode(7)
m=TreeNode(1)
n=TreeNode(2)

c=TreeNode(20)
c.left=a
c.right=b
d=TreeNode(9)
d.left=m
d.right=n
e=TreeNode(3)
e.left=d
e.right=c
tree1=Solution().levelOrderBottom(e)
print(tree1)
