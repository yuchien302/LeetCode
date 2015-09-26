import unittest


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums[:] = nums[(n-k):] + nums[:(n-k)]


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        nums = [1, 2]
        self.solution.rotate(nums, 1)
        self.assertListEqual(nums, [2, 1])

    def test_1(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        self.solution.rotate(nums, 3)
        self.assertListEqual(nums, [5, 6, 7, 1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
