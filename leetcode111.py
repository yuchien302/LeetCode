import unittest

from Tree import *

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        elif root.left is None and root.right is None:
            return 1

        elif root.left is None:
            return 1 + self.minDepth(root.right)

        elif root.right is None:
            return 1 + self.minDepth(root.left)

        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        t = Tree([1,2])
        self.assertEqual(self.solution.minDepth(t.root), 2)


if __name__ == '__main__':
    unittest.main()
