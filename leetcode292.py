import unittest


class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n%4 != 0


class Test(unittest.TestCase):
    def test_0(self):
        self.assertEqual(Solution().canWinNim(5), True)


if __name__ == '__main__':
    unittest.main()
