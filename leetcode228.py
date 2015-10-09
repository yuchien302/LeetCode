import unittest


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        result = [[0, 0]]
        final_result = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                result[-1][-1] += 1
            else:
                result += [[i, i]]

        for [start, end] in result:
            if start == end:
                final_result.append(str(nums[start]))
            else:
                final_result.append(str(nums[start]) + "->" + str(nums[end]))

        return final_result


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        ranges = self.solution.summaryRanges([0,1,2,4,5,7])
        self.assertListEqual(ranges, ["0->2","4->5","7"])


if __name__ == '__main__':
    unittest.main()
