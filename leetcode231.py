import unittest


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n & (n-1) == 0) and bool(n)


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        self.assertEqual(self.solution.isPowerOfTwo(4), True)

    def test_1(self):
        self.assertEqual(self.solution.isPowerOfTwo(3), False)

    def test_2(self):
        self.assertEqual(self.solution.isPowerOfTwo(0), False)

if __name__ == '__main__':
    unittest.main()
