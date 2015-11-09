# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtreesHelper(self, root):
        if not root:
            return 0, None

        (count1, val1) = self.countUnivalSubtreesHelper(root.left)
        (count2, val2) = self.countUnivalSubtreesHelper(root.right)
        count = count1 + count2
        val = None
        
        if not root.left and not root.right:
            return (count + 1, root.val)
            
        elif root.left and not root.right:
            if val1 == root.val:
                return (count + 1, root.val)
                
        elif not root.left and root.right:
            if val2 == root.val:
                return (count + 1, root.val)

        else:
            if root.left.val == root.right.val == root.val:
                return (count + 1, root.val)
                
        return count, val
        
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count, _ = self.countUnivalSubtreesHelper(root)
        return count
        