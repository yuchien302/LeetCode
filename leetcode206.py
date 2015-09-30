import unittest
from List import List, ListNode


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        return prev


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        my_raw_list = List([1, 2, 3, 4, 5])
        head = self.solution.reverseList(my_raw_list.head)

        self.assertListEqual(List.to_list(head), [5, 4, 3, 2, 1])



if __name__ == '__main__':
    unittest.main()
