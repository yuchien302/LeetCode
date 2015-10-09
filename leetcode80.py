import unittest


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        if len(nums) <= 2:
            return len(nums)

        pos = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[pos-2]:
                nums[pos] = nums[i]
                pos += 1

        return pos



class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        nums = self.solution.removeDuplicates([0, 0, 0, 1, 1, 1, 2, 3])
        self.assertEqual(nums, 6)


if __name__ == '__main__':
    unittest.main()