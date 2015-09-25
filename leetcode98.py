import unittest
from Tree import Tree, TreeNode


class Solution(object):
    def is_valid_bst(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = []
        self.in_order_traversal(result, root)
        return result == sorted(result) and len(set(result)) == len(result)

    def in_order_traversal(self, result, root):
        if root is None:
            return

        self.in_order_traversal(result, root.left)
        result.append(root.val)
        self.in_order_traversal(result, root.right)


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        t = Tree([2,1])
        self.assertEqual(self.solution.is_valid_bst(t.root), True)

    def test_1(self):
        t = Tree([1,2])
        self.assertEqual(self.solution.is_valid_bst(t.root), False)

    def test_2(self):
        t = Tree([1,1])
        self.assertEqual(self.solution.is_valid_bst(t.root), False)


if __name__ == '__main__':
    unittest.main()
