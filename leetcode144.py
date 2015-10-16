# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversalHelper(self, root, preorder):
        """
        :type root: TreeNode
        :rtype: None
        """
        if root:
            preorder.append(root.val)

            if root.left:
                self.preorderTraversalHelper(root.left, preorder)

            if root.right:
                self.preorderTraversalHelper(root.right, preorder)

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        preorder = []
        self.preorderTraversalHelper(root, preorder)
        return preorder

