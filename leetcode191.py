import unittest


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        if n == 0:
            return 0
        while n != 0:
            n &= (n-1)
            count += 1
        return count


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        self.assertEqual(self.solution.hammingWeight(4), 1)

    def test_1(self):
        self.assertEqual(self.solution.hammingWeight(3), 2)

    def test_2(self):
        self.assertEqual(self.solution.hammingWeight(0), 0)

if __name__ == '__main__':
    unittest.main()
