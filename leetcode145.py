import unittest

from Tree import *

class Solution(object):

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.makePostorder(result, root)
        return result

    def makePostorder(self, result, node):
        if node is None:
            return
        if node.left:
            self.makePostorder(result, node.left)
        if node.right:
            self.makePostorder(result, node.right)
        result.append(node.val)


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        t = Tree([1,None,2, None, None, 3])
        self.assertEqual(self.solution.postorderTraversal(t.root), [3,2,1])


if __name__ == '__main__':
    unittest.main()
