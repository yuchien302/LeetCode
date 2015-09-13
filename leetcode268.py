__author__ = 'yuchien'

import unittest

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n*(n+1)/2 - sum(nums)


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        paths = self.solution.missingNumber([0, 1, 2, 3, 5, 6, 7])
        self.assertEqual(paths, 4)



if __name__ == '__main__':
    unittest.main()
