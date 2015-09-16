import unittest
from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        d = deque([root])
        results = []
        while len(d) > 0:
            layer = []
            for _ in range(len(d)):
                node = d.popleft()
                layer.append(node.val)
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            results.append(layer)

        for i in range(len(results)):
            if i%2==1:
                results[i] = results[i][::-1]

        return results




class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        results = self.solution.zigzagLevelOrder(None)
        self.assertListEqual(results, [])

    def test_1(self):
        root = TreeNode(3)
        # {3,9,20,#,#,15,7},
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        results = self.solution.zigzagLevelOrder(root)
        self.assertListEqual(results, [[3],[20,9],[15,7]])





if __name__ == '__main__':
    unittest.main()


__author__ = 'yuchien'
