# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def count(node):
            return 0 if not node else 1 + count(node.left) + count(node.right)
        
        if not root:
            return
        
        left_count = count(root.left)
        if k <= left_count:
            return self.kthSmallest(root.left, k)
        elif k == left_count+1:
            return root.val
        else:
            return self.kthSmallest(root.right, k-left_count-1)
            