import unittest
from List import List, ListNode


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        my_raw_list = List([1, 2, 3, 4, 5])
        self.solution.deleteNode(my_raw_list.nodes[2])

        self.assertListEqual(List.to_list(my_raw_list.head), [1, 2, 4, 5])



if __name__ == '__main__':
    unittest.main()
