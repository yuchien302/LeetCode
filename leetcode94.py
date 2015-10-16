# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def inorderTraversalHelper(self, root, inorder):
        """
        :type root: TreeNode
        :rtype: None
        """
        if root:

            if root.left:
                self.inorderTraversalHelper(root.left, inorder)
                
            inorder.append(root.val)
            
            if root.right:
                self.inorderTraversalHelper(root.right, inorder)        
        
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        inorder = []
        self.inorderTraversalHelper(root, inorder)
        return inorder