# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxSinglePathSum(self, root):
        left, right = 0, 0
        if root is None:
            return 0
        if root.left:
            left = self.maxSinglePathSum(root.left)
        if root.right:
            right = self.maxSinglePathSum(root.right)
            
            
        return max(root.val, root.val + left, root.val + right, 0)
        
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return max( root.val + self.maxSinglePathSum(root.left) + self.maxSinglePathSum(root.right),
                    self.maxPathSum(root.left),
                    self.maxPathSum(root.right) )

        