# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return []
        if not root.left and not root.right and root.val == sum:
            return [[sum]]
            
        if root.left:
            res.extend( [[root.val] + p for p in self.pathSum(root.left, sum - root.val)] )
            
        if root.right:
            res.extend( [[root.val] + p for p in self.pathSum(root.right, sum - root.val)] )            
            
        return res