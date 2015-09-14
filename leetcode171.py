import unittest

__author__ = 'yuchien'


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        for i in s:
            num = num*26 + ord(i) - ord('A') + 1
        return num


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        num = self.solution.titleToNumber("AB")
        self.assertEqual(num, 28)

    def test_1(self):
        num = self.solution.titleToNumber("A")
        self.assertEqual(num, 1)

    def test_2(self):
        num = self.solution.titleToNumber("")
        self.assertEqual(num, 0)

if __name__ == '__main__':
    unittest.main()
