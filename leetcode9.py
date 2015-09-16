import unittest


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x)[::-1] == str(x)


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        pal = self.solution.isPalindrome(12321)
        self.assertEqual(pal, True)

    def test_1(self):
        pal = self.solution.isPalindrome(-13)
        self.assertEqual(pal, False)


if __name__ == '__main__':
    unittest.main()


__author__ = 'yuchien'
