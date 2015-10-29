# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        val = 0
            
        if root.left and target < root.val:
            val = min( [root.val, self.closestValue(root.left, target)], key=lambda val: abs(target-val) )
            
        elif root.right and target > root.val:
            val = min( [root.val, self.closestValue(root.right, target)], key=lambda val: abs(target-val) )
            
        else:
            val = root.val
            
        
        return val
            
        