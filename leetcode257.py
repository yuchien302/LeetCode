# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePathsHelper(self, root, s):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ans = []
        if root.left:
            ans += self.binaryTreePathsHelper(root.left, s + "->" + str(root.left.val))
            
        if root.right:
            ans += self.binaryTreePathsHelper(root.right, s + "->" + str(root.right.val))
            
        if root.left is None and root.right is None:
            ans = [s]
        
        return ans
        
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        return self.binaryTreePathsHelper(root, str(root.val))
        