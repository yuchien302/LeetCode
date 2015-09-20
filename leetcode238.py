import unittest


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1] * len(nums)
        fromBegin = 1
        fromEnd = 1
        for i in range(len(nums)):
            result[i] *= fromBegin
            fromBegin *= nums[i]

        for i in reversed(range(len(nums))):
            result[i] *= fromEnd
            fromEnd *= nums[i]

        return result


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        self.assertListEqual(self.solution.productExceptSelf([1, 2, 3, 4]), [24,12,8,6])



if __name__ == '__main__':
    unittest.main()
