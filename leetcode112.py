import unittest

from Tree import *

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False

        sum -= root.val

        if (sum == 0) and (root.left is None) and (root.right is None):
            return True

        else:
            return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        t = Tree([4, 2, 3, 1, None, None, 9])
        self.assertEqual(self.solution.hasPathSum(t.root, 7), True)

    def test_1(self):
        t = Tree([1,2,2,3,3,3,3,4,4,4,4,4,4,None,None,5,5])
        self.assertEqual(self.solution.hasPathSum(t.root, 10), True)


if __name__ == '__main__':
    unittest.main()
