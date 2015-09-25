import unittest
from List import List, ListNode


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        result = []
        node = head
        while node is not None:
            result.append(node)
            node = node.next

        result = sorted(result, key=lambda n: n.val)

        for i in range(1, len(result)):
            result[i-1].next = result[i]

        result[-1].next = None
        return result[0]



class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        my_raw_list = List([3, 5, 1, 4, 6])
        my_head = self.solution.sortList(my_raw_list.head)
        my_list = List.to_list(my_head)

        self.assertListEqual(my_list, [1, 3, 4, 5, 6])

    def test_1(self):
        my_raw_list = List([2, 1])
        my_head = self.solution.sortList(my_raw_list.head)
        my_list = List.to_list(my_head)

        self.assertListEqual(my_list, [1, 2])

if __name__ == '__main__':
    unittest.main()
