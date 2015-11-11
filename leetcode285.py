# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorder(self, root):
        if not root:
            return
        
        for n in self.inorder(root.left):
            yield n
            
        yield root
        
        for n in self.inorder(root.right):
            yield n
            
    
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        findp = False
        for n in self.inorder(root):
            if findp:
                return n
                
            if n == p:
                findp = True

        return None
            