import unittest

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self, vals):
        if len(vals) == 0:
            return

        self.nodes = []
        for i in range(len(vals)):
            if vals[i]:
                self.nodes.append(TreeNode(vals[i]))
            else:
                self.nodes.append(None)

        for i in range(len(vals)):
            if not self.nodes[i]:
                continue

            if i*2+1 < len(vals):
                self.nodes[i].left = self.nodes[i*2+1]

            if i*2+2 < len(vals):
                self.nodes[i].right = self.nodes[i*2+2]

        self.nodes = list(filter(lambda n: n is not None, self.nodes))
        self.root = self.nodes[0]




    def printPostOrder(self):
        self.printPostOrderHelper(self.root)

    def printPostOrderHelper(self, node):
        if not node:
            return
        if node.left:
            self.printPostOrderHelper(node.left)
        if node.right:
            self.printPostOrderHelper(node.right)
        print(node.val)


class Test(unittest.TestCase):
    # def setUp(self):
    #     self.solution = Solution()

    def test_0(self):
        t = Tree([1, 2, 3, 4, 5, 6, 7])

        self.assertEqual(t.root.val, 1)
        self.assertEqual(t.root.left.val, 2)
        self.assertEqual(t.root.right.val, 3)

    def test_1(self):
        t = Tree([1,None,2, None, None, 3])

        self.assertEqual(t.root.val, 1)
        self.assertEqual(t.root.left, None)
        self.assertEqual(t.root.right.val, 2)
        self.assertEqual(len(t.nodes), 3)


if __name__ == '__main__':
    unittest.main()