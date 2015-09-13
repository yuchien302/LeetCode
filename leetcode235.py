__author__ = 'yuchien'

import unittest

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p == q:
            return p

        if p.val > q.val:
            p, q = q, p

        if (p.val < root.val) and (root.val < q.val):
            return root

        if (p is root) or (q is root):
            return root

        if (p.val < root.val) and (q.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)





class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def printTree(self, root):

        print(root.val, end='')
        if root.left:
            print(', (', end='')
            self.printTree(root.left)
        if root.right:
            print(', (', end='')
            self.printTree(root.right)
        print(')', end='')
        # while

    def test_1(self):
        root = TreeNode(10)
        a1 =  TreeNode(5)
        a2 =  TreeNode(3)
        a3 =  TreeNode(6)
        a4 =  TreeNode(15)
        a5 =  TreeNode(12)
        root.left = a1
        root.left.left = a2
        root.left.right = a3
        root.right = a4
        root.right.left = a5

        self.printTree(root)
        parent = self.solution.lowestCommonAncestor(root, a2, a3)
        self.assertEqual(parent, a1)


if __name__ == '__main__':
    unittest.main()