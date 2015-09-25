import unittest


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class List(object):
    def __init__(self, vals):
        self.nodes = []
        self.current = 0

        if len(vals) == 0:
            self.head = None
            return

        self.nodes.append(ListNode(vals[0]))
        for i in range(1, len(vals)):
            self.nodes.append(ListNode(vals[i]))
            self.nodes[i-1].next = self.nodes[i]

        self.head = self.nodes[0]

    @staticmethod
    def to_list(head):
        result = []
        node = head
        while node is not None:
            result.append(node.val)
            node = node.next
        return result

class Test(unittest.TestCase):
    # def setUp(self):
    #     self.solution = Solution()

    def test_0(self):
        mylist = List([1, 2, 3, 4, 5, 6, 7])

        self.assertEqual(mylist.head.val, 1)
        self.assertEqual(mylist.head.next.val, 2)
        self.assertEqual(mylist.head.next.next.val, 3)

    def test_1(self):
        mylist = List([])
        self.assertEqual(mylist.head, None)


if __name__ == '__main__':
    unittest.main()