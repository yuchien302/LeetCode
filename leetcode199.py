# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        q = deque()
        q.append(root)
        result = []
        
        while len(q) != 0:
            result.append(0)
            n = len(q)
            for i in range(n):
                node = q.popleft()
                result[-1] = node.val
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                    
        return result
        