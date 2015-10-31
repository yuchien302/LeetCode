# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def longestConsecutiveHelper(self, root, prev_val, length):
        if root is None:
            return length
        
        if root.val == prev_val+1:
            length += 1
        else:
            length = 1
        
        return max(length, self.longestConsecutiveHelper(root.left, root.val, length), self.longestConsecutiveHelper(root.right, root.val, length))
    
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.longestConsecutiveHelper(root.left, root.val, 1), self.longestConsecutiveHelper(root.right, root.val, 1))
        