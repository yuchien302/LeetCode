import unittest


class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for _ in range(32):
            result <<= 1
            result |= (n & 1)
            n >>= 1
        return result

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        self.assertEqual(self.solution.reverseBits(43261596), 964176192)

    def test_1(self):
        self.assertEqual(self.solution.reverseBits(0), 0)


if __name__ == '__main__':
    unittest.main()
