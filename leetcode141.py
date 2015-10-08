import unittest
from List import *

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        fast = head.next
        slow = head

        while fast is not None:
            if fast == slow:
                return True
            if fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
        return False


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        n1 = ListNode(3)
        n2 = ListNode(4)
        n3 = ListNode(3)
        n4 = ListNode(4)
        n1.next = n2
        n2.next = n3
        n3.next = n4
        n4.next = n2
        self.assertEqual(Solution().hasCycle(n1), True)



if __name__ == '__main__':
    unittest.main()
