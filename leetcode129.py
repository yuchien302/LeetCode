import unittest
from Tree import Tree, TreeNode


class Solution(object):
    def __init__(self):
        self.res = 0

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.dfs(0, root)
        return self.res

    def dfs(self, current_num, root):
        if root is None:
            return
        num = 10*current_num + root.val
        self.dfs(num, root.left)
        self.dfs(num, root.right)
        if root.left is None and root.right is None:
            self.res += num


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        t = Tree([1, 2, 3])
        self.assertEqual(self.solution.sumNumbers(t.root), 25)


if __name__ == '__main__':
    unittest.main()
