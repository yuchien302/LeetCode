import unittest


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums)==0 :
            return 0

        pos = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[pos-1]:
                nums[pos] = nums[i]
                pos += 1

        return pos


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        nums = self.solution.removeDuplicates([0, 0, 1, 2, 3])
        self.assertEqual(nums, 4)


if __name__ == '__main__':
    unittest.main()