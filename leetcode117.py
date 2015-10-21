# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
from collections import deque
class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root is None:
            return 
        q = deque([root])
        while len(q) != 0:
            n = len(q)
            
            for i in range(n):
                node = q.popleft()
                if i != n-1:
                    node.next = q[0]
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            