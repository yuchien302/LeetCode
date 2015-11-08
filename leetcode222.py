# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math

class Solution(object):
    def getDepth(self, node):
        count = 0
        while node:
            node = node.left
            count += 1
        return count
            

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        ld = self.getDepth(root.left)
        rd = self.getDepth(root.right)
        
        if ld == rd:
            return 1 + (int(math.pow(2, ld)) - 1) + self.countNodes(root.right)
        else:
            return 1 + self.countNodes(root.left) + (int(math.pow(2, rd)) - 1)
            
        
    
