import unittest


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0

        while n > 0:
            count += (n//5)
            n /= 5
        return count


class Test(unittest.TestCase):
    def test_0(self):
        self.assertEqual(Solution().trailingZeroes(6), 1)


if __name__ == '__main__':
    unittest.main()
