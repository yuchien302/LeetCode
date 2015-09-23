import unittest


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        sum = 0
        min_arrlen = len(nums)+1
        for i in range(0, len(nums)):
            sum += nums[i]

            while sum >= s:
                min_arrlen = min(min_arrlen, i-start+1)
                sum -= nums[start]
                start += 1

        return min_arrlen if min_arrlen != (len(nums)+1) else 0




class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        self.assertEqual(self.solution.minSubArrayLen(7, [2,3,1,2,4,3]), 2)

    def test_1(self):
        self.assertEqual(self.solution.minSubArrayLen(11, [1,2,3,4,5]), 3)


if __name__ == '__main__':
    unittest.main()
