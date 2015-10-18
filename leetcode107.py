# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        ans = []
        queue = deque([root])
        while len(queue) != 0:
            ans.append([])
            for i in range(len(queue)):
                n = queue.popleft()
                ans[-1].append(n.val)
                if n.left is not None:
                    queue.append(n.left)
                    
                if n.right is not None:
                    queue.append(n.right)

        return list(reversed(ans))
        
        