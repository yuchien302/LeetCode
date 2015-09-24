import unittest

from Tree import *

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        left_max = self.height(root.left)
        right_max = self.height(root.right)
        # print(left_max, left_min, right_max, right_min)
        return (abs(left_max - right_max) <= 1) and self.isBalanced(root.left) and self.isBalanced(root.right)


    def height(self, node):
        if node is None:
            return 0
        left_max = self.height(node.left)
        right_max = self.height(node.right)

        return 1 + max(left_max, right_max)




class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        t = Tree([4, 2, 3, 1, None, None, 9])
        self.assertEqual(self.solution.isBalanced(t.root), True)


    def test_1(self):
        t = Tree([4, 2, None, 1, 3])
        self.assertEqual(self.solution.isBalanced(t.root), False)

    def test_2(self):
        t = Tree([1,2,2,3,None,None,3,4,None,None,4])
        self.assertEqual(self.solution.isBalanced(t.root), False)

    def test_3(self):
        t = Tree([1,2,2,3,3,3,3,4,4,4,4,4,4,None,None,5,5])
        self.assertEqual(self.solution.isBalanced(t.root), True)


if __name__ == '__main__':
    unittest.main()
