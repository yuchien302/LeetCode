__author__ = 'yuchien'

import unittest

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        else:
            n = num % 9
            return n if n != 0 else 9


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        paths = self.solution.addDigits(38)
        self.assertEqual(paths, 2)

    def test_2(self):
        paths = self.solution.addDigits(8149)
        self.assertEqual(paths, 4)

    def test_3(self):
        paths = self.solution.addDigits(9)
        self.assertEqual(paths, 9)

    def test_4(self):
        paths = self.solution.addDigits(18)
        self.assertEqual(paths, 9)

    def test_5(self):
        paths = self.solution.addDigits(0)
        self.assertEqual(paths, 0)

if __name__ == '__main__':
    unittest.main()

