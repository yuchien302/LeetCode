import unittest


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        current_min = x if len(self.stack) == 0 or x < self.getMin() else self.getMin()
        self.stack.append((x, current_min))

    def pop(self):
        """
        :rtype: nothing
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]


class Test(unittest.TestCase):

    def test_0(self):
        s = MinStack()
        s.push(-3)
        s.push(-5)
        self.assertEqual(s.getMin(), -5)
        s.pop()
        self.assertEqual(s.getMin(), -3)


if __name__ == '__main__':
    unittest.main()
