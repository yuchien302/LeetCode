# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def f(self, root, prev_val, length):
        if root is None:
            return length
        
        if root.val == prev_val+1:
            length += 1
        else:
            length = 1
        
        return max(length, self.f(root.left, root.val, length), self.f(root.right, root.val, length))
    
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.f(root.left, root.val, 1), self.f(root.right, root.val, 1))


    # def f(self, root, force_include, dict):
    #     if (root, force_include) in dict:
    #         return dict[(root, force_include)]
    #
    #     if root is None:
    #         return 0
    #
    #     if force_include:
    #         left = right = 0
    #         if root.left and root.left.val == root.val + 1:
    #             left = self.f(root.left, True, dict) + 1
    #
    #         if root.right and root.right.val == root.val + 1:
    #             right = self.f(root.right, True, dict) + 1
    #
    #         dict[(root, force_include)] = max(1, left, right)
    #         return max(1, left, right)
    #     else:
    #         left = self.f(root.left, False, dict)
    #         right = self.f(root.right, False, dict)
    #         current = self.f(root, True, dict)
    #         dict[(root, force_include)] = max(current, left, right)
    #         return max(current, left, right)
    #
    # def longestConsecutive(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     if not root:
    #         return 0
    #     dict = {}
    #     return self.f(root, False, dict)