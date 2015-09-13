__author__ = 'yuchien'

import unittest

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        sortedCits = sorted(citations, reverse=True)
        n = len(citations)
        if n == 0 or sortedCits[0] == 0:
            return 0

        if n == 1:
            return 1

        for i in range(1, n):
            if sortedCits[i] <= i:
                return i

        return n


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        hIndex = self.solution.hIndex([])
        self.assertEqual(hIndex, 0)

    def test_1(self):
        hIndex = self.solution.hIndex([3, 0, 6, 1, 5])
        self.assertEqual(hIndex, 3)

    def test_2(self):
        hIndex = self.solution.hIndex([0])
        self.assertEqual(hIndex, 0)

    def test_3(self):
        hIndex = self.solution.hIndex([1])
        self.assertEqual(hIndex, 1)

    def test_4(self):
        hIndex = self.solution.hIndex([4, 0, 6, 1, 5])
        self.assertEqual(hIndex, 3)

    def test_5(self):
        hIndex = self.solution.hIndex([11, 15])
        self.assertEqual(hIndex, 2)


if __name__ == '__main__':
    unittest.main()
